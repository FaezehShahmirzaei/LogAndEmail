import logging

from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger("myproject.custom")

class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.error('harchi shod')


