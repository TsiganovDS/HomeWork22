from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")
        permission = Permission.objects.get(codename="can_unpublish_product")
        group.permissions.add(Permission.objects.get(codename="can_delete_any_product"))
        group.permissions.add(permission)
        help = "Удаляет все продукты и категории, затем добавляет тестовые"

        Product.objects.all().delete()
        Category.objects.all().delete()

        cat1 = Category.objects.create(name="Ноутбуки", description="Мощные ноутбуки")
        cat2 = Category.objects.create(
            name="Смартфоны", description="Современные смартфоны"
        )
        cat3 = Category.objects.create(
            name="Планшеты", description="Планшетные компьютеры"
        )

        Product.objects.create(
            name="Apple MacBook Pro",
            description="Ноутбук для профессионалов",
            price=1999,
            category=cat1,
        )
        Product.objects.create(
            name="ASUS ZenBook",
            description="Лёгкий ультрабук",
            price=1200,
            category=cat1,
        )
        Product.objects.create(
            name="Samsung Galaxy S22",
            description="Флагманский смартфон",
            price=999,
            category=cat2,
        )
        Product.objects.create(
            name="Xiaomi Mi 12",
            description="Доступный смартфон",
            price=600,
            category=cat2,
        )
        Product.objects.create(
            name="Apple iPad Air",
            description="Функциональный планшет",
            price=800,
            category=cat3,
        )

        self.stdout.write(
            self.style.SUCCESS("Все тестовые продукты успешно добавлены!")
        )
