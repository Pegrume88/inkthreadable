import django_filters
from .models import Product
from django_filters import CharFilter


class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {'gender': ['exact'],
                  'category': ['exact'],
                  'name': ['icontains'],}
                                        

class ProductCategoryFilter(django_filters.FilterSet):
    
    class Meta:
        model = Product
        fields = {'gender': ['exact'],
                 
                  'name': ['icontains'],}
        
class SearchFilter(django_filters.FilterSet):
    name = CharFilter(label='search')
    class Meta:
        model = Product
        
        fields = ['name',]
        
    #def __init__(self, *args, **kwargs):
        #super(SearchFilter, self).__init__(*args, **kwargs)
        #self.filters['name'].extra.update(
            #{'empty_label': 'search'})
                                        

