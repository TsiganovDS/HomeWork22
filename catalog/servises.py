from catalog.models import Product


def get_products_by_category(category_id):
    try:
        products = Product.objects.filter(category_id=category_id).order_by("name")
        return products
    except Product.DoesNotExist:
        return []
