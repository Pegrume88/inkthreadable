import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {'gender': ['exact'],
                  'category': ['exact'],
                  'name': ['icontains'],}
                                        

class SearchFilter(django_filters.FilterSet):
   
    class Meta:
        model = Product
        fields = {
                   }