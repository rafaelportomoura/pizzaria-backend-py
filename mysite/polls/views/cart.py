def cart(request):
    cart = OrderService().getCartOrder()
    return cart
