def __components__(path):
    return f"components/{path}"


def __view__(path):
    return f"views/{path}"


WORK_IN_PROGRESS = __components__("work_in_progress.html")
LOGIN = __view__("login.html")
PRODUCTS = __view__("products.html")
INDEX = __view__("index.html")
CART = __view__("cart.html")
CLIENT = __view__("client.html")
