from django import forms
from . import models


class canvasForm(forms.ModelForm):
    class Meta:
        model = models.usercanvas
        fields = ['questions']