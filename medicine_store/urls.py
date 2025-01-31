# store/urls.py
from django.urls import path
from . import views

app_name = 'medicine_store'

urlpatterns = [
    path('', views.store_view, name='store_view'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('filter-products/', views.filter_medicines, name='filter_products'),
   #  path('category/<int:id>/<slug:slug>/', views.category_detail, name='category_detail')
    
]

