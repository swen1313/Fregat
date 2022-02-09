from django import forms

from .models import Park

class ParkForm(forms.ModelForm):

    class Meta:
        model = Park
        fields = ("place", "time")


