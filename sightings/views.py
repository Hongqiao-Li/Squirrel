from django.shortcuts import render, redirect
from .models import SqurInfo
from .forms import SqurForm
from django.shortcuts import get_object_or_404
from django.db.models import Count

# Create your views here.


def squrshow(request):
    squrs = SqurInfo.objects.all()
    context = {'squrs': squrs}
    return render(request, 'sightings/show.html', context)


def detail(request, squr_id):
    squr = get_object_or_404(SqurInfo, unique_squirrel_id=squr_id)
    if request.method == 'POST':
        form = SqurForm(request.POST, instance=squr)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SqurForm(instance=squr)
    context = {'form': form}

    return render(request, 'sightings/detail.html', context)


def squradd(request):
    if request.method == 'POST':
        form = SqurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SqurForm()
    context = {'form': form}
    return render(request, 'sightings/add.html', context)


def stats(request):
    total = SqurInfo.objects.count()
    fur_color_count = SqurInfo.objects.values(
        'primary_fur_color').annotate(c=Count('primary_fur_color'))
    shift_count = SqurInfo.objects.values('shift').annotate(c=Count('shift'))
    location_count = SqurInfo.objects.values('location').annotate(c=Count('location'))
    age_count = SqurInfo.objects.values('age').annotate(c=Count('age'))
    context = {
        'total': total,
        'fur_black_count': fur_color_count[0]['c'],
        'fur_cinnamon_count': fur_color_count[1]['c'],
        'fur_gray_count': fur_color_count[2]['c'],
        'shift_AM_count': shift_count[0]['c'],
        'shift_PM_count': shift_count[1]['c'],
        'location_AG_count': location_count[0]['c'],
        'location_GP_count': location_count[1]['c'],
        'age_adult_count': age_count[1]['c'],
        'age_juvenile_count': age_count[2]['c'],
    }

    return render(request, 'sightings/stats.html', context)
