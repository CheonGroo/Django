from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll
from polls import models

class Command(BaseCommand):
    help = 'Create Post'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str)
        parser.add_argument('content', type=str)

    def handle(self, *args, **options):
        q = models.Question.objects.create(title=options['title'],content=options['content'])
        q.save()
        self.stdout.write(self.style.SUCCESS(f'Successfully Create Post "{q.id}"'))