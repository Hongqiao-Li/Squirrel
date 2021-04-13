from django.forms import ModelForm
from .models import SqurInfo


class SqurForm(ModelForm):
    class Meta:
        model = SqurInfo
        fields = '__all__'

