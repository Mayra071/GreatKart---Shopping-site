from django.shortcuts import render
from store.models import Product
from cart.views import _cart_id
from cart.models import Cart, CartItem
from django.core.paginator import Paginator

def home(request):
    products = Product.objects.all().filter(is_available=True)
    
    # Get cart items to check which products are in cart
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        in_cart_products = [item.product.id for item in cart_items]
    except:
        in_cart_products = []

    # Add pagination
    paginator = Paginator(products, 8)  # Show 8 products per page
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'in_cart_products': in_cart_products,
    }
    return render(request, 'home.html', context=context)