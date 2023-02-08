import django_filters
from .models import Product
from django_filters import CharFilter


class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {'gender': ['exact'],
                  'category': ['exact'],
                  'name': ['icontains'],}
                                        

