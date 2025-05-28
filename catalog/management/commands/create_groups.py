from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов"'

    def handle(self, args, *options):
        self.stdout.write("Создается группа 'Модератор продуктов'...")
        create_product_moderator_group()
        self.stdout.write(self.style.SUCCESS("Группа 'Модератор продуктов' создана"))


def create_product_moderator_group():
    (group,) = Group.objects.get_or_create(name="Модератор продуктов")
    content_type = ContentType.objects.getfor_model(Product)
    permissions = Permission.objects.filter(
        content_type=content_type,
        codename_in=["can_unpublish_product", "delete_product"],
    )
    group.permissions.set(permissions)
    group.save()
