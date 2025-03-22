from django.core.management.base import BaseCommand
from accounts.models import Account

class Command(BaseCommand):
    help = 'List all users in the database'

    def handle(self, *args, **kwargs):
        users = Account.objects.all()
        for user in users:
            self.stdout.write(f'Email: {user.email}, Username: {user.username}, Password: {user.password}')
