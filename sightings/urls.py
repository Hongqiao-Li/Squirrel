from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.squrshow),
    path('add/', views.squradd, name='add'),
    path('stats/', views.stats, name='stats'),
    path('<squr_id>/', views.detail, name='detail'),
]

