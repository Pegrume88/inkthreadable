from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=False, blank=False, unique=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    users_wishlist = models.ManyToManyField(
        User, related_name='users_wishlist', blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def get_rating(self):
        total_rating = 0
        
        for review in Review.objects.filter(product=self) :
            total_rating += review.rating
            
        if total_rating > 0:
            return total_rating / self.reviews.count()
            
        return total_rating
        
    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'


class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='like_product')
    user = models.ManyToManyField(User)

