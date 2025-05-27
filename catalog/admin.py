from django.contrib import admin
from django.apps import AppConfig
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


from users.models import CustomUser
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


def create_permissions():
    contenttype = ContentType.objects.getfor_model(Product)
    permission, created = Permission.objects.getorcreate(
        codename='can_unpublish_product',
        name='Can unpublish product',
        contenttype=contenttype
    )

    user_email = 'dm.tsiganov@gmail.com'
    try:
        user = CustomUser.objects.get(email=user_email)
        user.user_permissions.add(permission)
    except CustomUser.DoesNotExist:
        print(f"Пользователь с email {user_email} не найден.")


class ProductConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        create_permissions()





