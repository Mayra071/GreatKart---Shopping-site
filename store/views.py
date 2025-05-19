from django.shortcuts import render,get_object_or_404
#from django.http import HttpResponse
from .models import Product
from category.models import Category
from cart.views import _cart_id
from cart.models import CartItem, Cart
from django.core.paginator import Paginator

def store(request, category_slug=None):
    products = None
    categories = None
    cart_items = None
    
    if category_slug is not None:
        categories = [get_object_or_404(Category, slug_field=category_slug)]
        products = Product.objects.filter(category=categories[0].id, is_available=True).order_by('id')
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        categories = list(Category.objects.all())
        product_count = products.count()

    # Add pagination
    paginator = Paginator(products, 6)  # Show 6 products per page
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    # Get cart items to check which products are in cart
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        in_cart_products = [item.product.id for item in cart_items]
    except:
        in_cart_products = []

    context = {
        'products': paged_products,
        'categories': categories,  
        'product_count': product_count,
        'in_cart_products': in_cart_products,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug_field=category_slug, slug_field=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
       # return HttpResponse(in_cart)
       # exit()
    except Product.DoesNotExist:
        single_product = None
    if single_product is None:
        return render(request, '404.html', status=404)
    
    context= {
        'single_product': single_product,
        'in_cart': in_cart,
        # 'categories': Category.objects.all(),
    }
    return render(request, 'store/product_detail.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(product_name__icontains=keyword) | Product.objects.filter(description__icontains=keyword)
            product_count = products.count()
    else:
        products = Product.objects.none()
        product_count = 0
    
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
    