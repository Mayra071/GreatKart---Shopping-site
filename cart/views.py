from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    # Get the referring URL (the page the user was on when they clicked "Add to Cart")
    referer = request.META.get('HTTP_REFERER')
    
    product = get_object_or_404(Product, id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.warning(request, f"Sorry, only {product.stock} items available in stock!")
    except CartItem.DoesNotExist:
        if product.stock > 0:
            cart_item = CartItem.objects.create(
                product=product,
                quantity=1,
                cart=cart
            )
            cart_item.save()
        else:
            messages.warning(request, "Sorry, this product is out of stock!")
    if referer:
        return HttpResponseRedirect(referer)
    return redirect('cart')

def remove_cart(request, product_id):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        messages.warning(request, "Item not found in your cart!")
    return redirect('cart')

def remove_cart_item(request, product_id):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.delete()
        messages.success(request, "Item removed from your cart!")
    except (Cart.DoesNotExist, CartItem.DoesNotExist):
        messages.warning(request, "Item not found in your cart!")
    return redirect('cart')

def cart(request):
    total = 0
    quantity = 0
    cart_items = None
    tax = 0
    grand_total = 0
    
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            item_total = cart_item.product.price * cart_item.quantity
            total += item_total
            quantity += cart_item.quantity
            # Add item_total to cart_item for template use
            cart_item.item_total = item_total
        
        # Calculate tax (18% GST)
        tax = (total * 0.18)
        # Calculate grand total
        grand_total = total + tax
        
    except ObjectDoesNotExist:
        pass
    
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax': tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)