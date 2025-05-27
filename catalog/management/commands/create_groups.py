from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        create_product_moderator_group()
        print("Группа 'Модератор продуктов' создана")


def create_product_moderator_group():
    group, _ = Group.objects.get_or_create(name='Модератор продуктов')
    content_type = ContentType.objects.get_for_model(Product)
    permissions = Permission.objects.filter(
        content_type=content_type,
        codename__in=['can_unpublish_product', 'can_delete_any_product']
    )
    group.permissions.set(permissions)
    group.save()

create_product_moderator_group()