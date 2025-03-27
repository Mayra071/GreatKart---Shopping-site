from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
def store(request, category_slug=None):
    products=None
    categories=None
    if category_slug is not None:
        categories = [get_object_or_404(Category, slug_field=category_slug)]  # Wrap in a list
        products = Product.objects.filter(category=categories[0].id, is_available=True)  # Use the ID
        product_count=products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        categories = list(Category.objects.all())  # Convert to list for consistency
        product_count=products.count()

        # Retrieve all categories
    context = {
        'products': products,
        'categories': categories,  # Add categories to context
        'product_count': product_count,  # Add product count to context


    }
    # Ensure this function is correctly implemented
    return render(request, 'store/store.html', context)
