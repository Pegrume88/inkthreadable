from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponseRedirect
from .models import Product, Category, Review, Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.db.models import Q
from django.contrib import messages
from .filters import ProductFilter, ProductCategoryFilter, SearchFilter
from .forms import ProductForm, ReviewForm


def category_products(request, category_id):

    products = Product.objects.filter(category__pk=category_id)
    product_filter = ProductCategoryFilter(request.GET, queryset=products)

    context = {
        'products': products,
        'product_filter': product_filter,



    }

    return render(request, 'products/products.html', context)


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    product_filter = ProductFilter(request.GET, queryset=products)
    search_filter = SearchFilter(request.GET, queryset=products)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'product_filter': product_filter,
        'search_filter': search_filter,


    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    try:
        product_like = Like.objects.get(product=product)
        liked = product_like is not None and request.user in product_like.user.all()
    except Exception as e:
        liked = False
    form = ReviewForm()

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(
                user=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    user=request.user
                )
                #return redirect('product')

    product_rating = product.get_rating()
    context = {
        'product': product,
        'product_rating': product_rating,
        'liked': liked
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "products/wishlist.html", {'wishlist': products})


@login_required()
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, product.name +
                         " has been removed from your WishList")
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, "Added " +
                         product.name + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


@login_required()
def like_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_likes, created = Like.objects.get_or_create(product=product)
    if request.user not in product_likes.user.all():
        product_likes.user.add(request.user)
        messages.success(request, product.name +
                         " has been liked")
    else:
        product_likes.user.remove(request.user)
        messages.success(request,
                         product.name + " disliked")
    product_likes.save()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

#def add_review(request, product_id):
    #product = get_object_or_404(Product, pk=product_id)
    #if request.method == 'POST':
        #form = ReviewForm(request.POST)
        #if form.is_valid():
        #    review = form.save(commit=False)
        #    review.product = product
        #    review.save()

    #return render(request, 'products/product_detail.html', context)
    