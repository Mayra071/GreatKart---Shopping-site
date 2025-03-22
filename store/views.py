
from django.shortcuts import render
from .models import Product
from category.models import Category
def store(request):
    products = Product.objects.all().filter(is_available=True)
    categories = Category.objects.all()  # Retrieve all categories
    context = {
        'products': products,
        'categories': categories,  # Add categories to context

    }
    # Ensure this function is correctly implemented
    return render(request, 'store/store.html', context)
