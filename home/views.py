from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def about(request):
    """ A view to return the index page """

    return render(request, 'about/about.html')


