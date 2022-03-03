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


class questionInputSelective(forms.ModelForm):
    class Meta:
        model = models.selectiveQuestion
        fields = ['classes', 'subject', 'chapter', 'scenario', 'ques_img', 'q_a', 'q_b', 'q_c', 'q_d']


class questionInputBijoySelective(forms.ModelForm):
    class Meta:
        model = models.selectiveQuestion
        fields = ['classes', 'subject', 'chapter', 'ques_img']


class userInformation(forms.ModelForm):
    class Meta:
        model = models.userInformation
        fields = ['institution']


class paymentInformation(forms.ModelForm):
    class Meta:
        model = models.paymentInformation
        fields = ['package', 'trxID']


class UserProfile(forms.ModelForm):
    class Meta:
        model = models.userProfile
        fields = ['user_name', 'user_phone', 'user_address', 'bio', 'user_image']


class DocumentQuestions(forms.ModelForm):
    class Meta:
        model = models.docQuestions
        fields = ['classes', 'subject', 'chapter', 'questionTitle', 'docs']


class EnglishDocQuestions(forms.ModelForm):
    class Meta:
        model = models.english_docQuestions
        fields = ['classes', 'paper', 'chapter', 'questionTitle', 'docs']


class ClassSuggesstion(forms.ModelForm):
    class Meta:
        model = models.class_suggesstion
        fields = ['classes', 'date', 'bangla', 'english', 'math', 'science', 'social', 'islamReligion', 'hinduReligion',
                  'boudhuReligion', 'cristantianReligion', 'artsAndCrafts', 'physicalEducation', 'music', 'comment']
