import csv
from django.core.management.base import BaseCommand, CommandError
from sightings.models import SqurInfo


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('args', type=str, nargs='*')

    def handle(self, *args, **kwargs):
        path = args[0]
        fields = SqurInfo._meta.fields
        with open(path, 'w') as f:
            writer = csv.writer(f)
            for i in SqurInfo.objects.all():
                row = [getattr(i, field.name) for field in fields]
                writer.writerow(row)
            f.close()
        print('Export successfully!')
