from django.urls import path
from .import views
urlpatterns = [
    path('', views.store, name='store'),  # Ensure this name matches the template reference

    path('<slug:category_slug>/', views.store, name='product_by_category'),
]
