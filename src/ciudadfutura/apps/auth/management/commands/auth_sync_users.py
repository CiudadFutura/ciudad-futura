# -- encoding: utf-8 --
from django.core.management.base import BaseCommand
from ciudadfutura.apps.auth.models import User


class Command(BaseCommand):

    help = 'Sync users with the old database.'

    def handle(self, *args, **kwargs):
        # User create/update
        pass
