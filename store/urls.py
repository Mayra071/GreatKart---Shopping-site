from django.urls import path
from .import views
urlpatterns = [
    path('', views.store, name='store'),  # Ensure this name matches the template reference
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/', views.store, name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),  # Ensure this name matches the template reference
]
