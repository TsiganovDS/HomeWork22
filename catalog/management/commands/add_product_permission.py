from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand, CommandError

from catalog.models import Product


class Command(BaseCommand):
    help = "Adds a specific permission to a user for the Product model"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str, help="User email")
        parser.add_argument(
            "permission_code_name", type=str, help="Permission code_name"
        )

    def handle(self, *args, **options):
        User = get_user_model()
        email = options["email"]
        permission_code_name = options["permission_code_name"]

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise CommandError(f'User with email "{email}" does not exist')

        try:
            content_type = ContentType.objects.get_for_model(Product)
            permission = Permission.objects.get(
                code_name=permission_code_name, content_type=content_type
            )
        except Permission.DoesNotExist:
            raise CommandError(
                f'Permission with code_name "{permission_code_name}" does not exist for Product model'
            )

        user.user_permissions.add(permission)
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully added permission "{permission_code_name}" to user "{email}"'
            )
        )
