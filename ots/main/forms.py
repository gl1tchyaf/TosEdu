from django import forms
from . import models


class questionInput(forms.ModelForm):
    class Meta:
        model = models.questions
        fields = ['classes', 'subject', 'chapter', 'scenario', 'ques_img', 'q_a', 'q_b', 'q_c', 'q_d']


class questionInputBijoy(forms.ModelForm):
    class Meta:
        model = models.questions
        fields = ['classes', 'subject', 'chapter', 'ques_img']

