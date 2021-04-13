import csv
import datetime
from django.core.management.base import BaseCommand, CommandError
from sightings.models import SqurInfo


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, encoding='utf-8') as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        for squr in data:
            squirrel = SqurInfo.objects.filter(unique_squirrel_id=squr['Unique Squirrel ID'])
            if squirrel.exists():
                print(f"{squr['Unique Squirrel ID']} has been recorded")
                continue

            squirrel, created = SqurInfo.objects.get_or_create(
                longitude=squr['X'],
                latitude=squr['Y'],
                unique_squirrel_id=squr['Unique Squirrel ID'],
                shift=squr['Shift'],
                date=datetime.datetime.strptime(squr['Date'].strip(), '%m%d%Y').date(),
                age='Unknown' if squr['Age'] == '' else squr['Age'],
                primary_fur_color='Unknown' if squr['Primary Fur Color'] == '' else squr['Primary Fur Color'],
                location='Unknown' if squr['Location'] == '' else squr['Location'],
                specific_location=squr['Specific Location'],
                running=True if squr['Running'] == 'TRUE' else False,
                chasing=True if squr['Chasing'] == 'TRUE' else False,
                climbing=True if squr['Climbing'] == 'TRUE' else False,
                eating=True if squr['Eating'] == 'TRUE' else False,
                foraging=True if squr['Foraging'] == 'TRUE' else False,
                other_activities=squr['Other Activities'],
                kuks=True if squr['Kuks'] == 'TRUE' else False,
                quaas=True if squr['Quaas'] == 'TRUE' else False,
                moans=True if squr['Moans'] == 'TRUE' else False,
                tail_flags=True if squr['Tail flags'] == 'TRUE' else False,
                tail_twitches=True if squr['Tail twitches'] == 'TRUE' else False,
                approaches=True if squr['Approaches'] == 'TRUE' else False,
                indifferent=True if squr['Indifferent'] == 'TRUE' else False,
                runs_from=True if squr['Runs from'] == 'TRUE' else False,
            )
            if created:
                squirrel.save()
                print(
                    f"Squirrel {squr['Unique Squirrel ID']} has been recorded.")
            else:
                raise ValueError("Something wrong in the data import!")

