from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class SqurInfo(models.Model):
    unique_squirrel_id = models.CharField(max_length=20)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICES = ((AM, 'AM'), (PM, 'PM'))
    shift = models.CharField(max_length=2, choices=SHIFT_CHOICES, default='Unknown')
    date = models.DateField(max_length=10)
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    Unknown = 'Unknown'
    AGE_CHOICES = ((ADULT, 'Adult'), (JUVENILE, 'Juvenile'), (Unknown, 'Unknown'))
    age = models.CharField(default='Unknown', max_length=20, choices=AGE_CHOICES)
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    GRAY = 'Gray'
    Unknown = 'Unknown'
    FUR_CHOICES = ((CINNAMON, 'Cinnamon'), (BLACK, 'Black'), (GRAY, 'Gray'), (Unknown, 'Unknown'))
    primary_fur_color = models.CharField(max_length=20, choices=FUR_CHOICES, default='Unknown')
    ABOVE = 'Above Ground'
    GROUND = 'Ground Plane'
    Unknown = 'Unknown'
    LOCATION_CHOICES = ((ABOVE, 'Above Ground'), (GROUND, 'Ground Plane'), (Unknown, 'Unknown'))
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='Unknown')
    specific_location = models.CharField(max_length=200, blank=True)
    running = models.BooleanField(help_text=_('Squirrel was seen running.'), default=False)
    chasing = models.BooleanField(help_text=_('Squirrel was seen chasing.'), default=False)
    climbing = models.BooleanField(help_text=_('Squirrel was seen climbing.'), default=False)
    eating = models.BooleanField(help_text=_('Squirrel was seen eating.'), default=False)
    foraging = models.BooleanField(help_text=_('Squirrel was seen foraging.'), default=False)
    other_activities = models.CharField(max_length=200, blank=True)
    kuks = models.BooleanField(help_text=_('Squirrel was heard kukking.'), default=False)
    quaas = models.BooleanField(help_text=_('Squirrel was heard quaaing.'), default=False)
    moans = models.BooleanField(help_text=_('Squirrel was heard moaning.'), default=False)
    tail_flags = models.BooleanField(help_text=_('Squirrel was seen flagging its tail.'), default=False)
    tail_twitches = models.BooleanField(help_text=_('Squirrel was seen twitching its tail.'), default=False)
    approaches = models.BooleanField(help_text=_('Squirrel was seen approaching human, seeking food.'), default=False)
    indifferent = models.BooleanField(help_text=_('Squirrel was indifferent to human presence.'), default=False)
    runs_from = models.BooleanField(help_text=_('Squirrel was running from humans, seeing them as a threat.'),
                                    default=False)

    def __str__(self):
        return self.unique_squrriel_id
