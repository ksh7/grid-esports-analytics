import os

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Resetting development database with dummy data...')

        # call_command('reset_db', '--noinput')
        call_command('migrate')
        call_command('loaddata', 'admin')
        call_command('loaddata', 'users')
