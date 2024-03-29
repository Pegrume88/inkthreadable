from django.urls import path
from . import views



urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<category_id>', views.category_products, name='category_products'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),   
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path("wishlist", views.wishlist, name="wishlist"),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='users_wishlist'),
    path('like/<int:product_id>/', views.like_product, name='like_product'),    
    ]