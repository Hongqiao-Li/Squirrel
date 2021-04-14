from django.shortcuts import render
from sightings.models import SqurInfo


# Create your views here.


def map(request):
    context = {"sightings": SqurInfo.objects.all()[:100]}
    return render(request, 'map/mapshow.html', context)
