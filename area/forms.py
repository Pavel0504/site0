from django.forms.utils import ErrorList

from .models import MainForm
from django.forms import ModelForm

from area.models import *


class AreaForm(ModelForm):
    class Meta:
        model = MainForm
        exclude = ["measure_unit", "user_create"]
