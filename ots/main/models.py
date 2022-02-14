from django.conf import settings
from django.db import models

CLASSSS_CHOICES = [
    (1, 'Class One'),
    (2, 'Class Two'),
    (3, 'Class Three'),
    (4, 'Class Four'),
    (5, 'Class Five'),
    (6, 'Class Six'),
    (7, 'Class Seven'),
    (8, 'Class Eight'),
    (9, 'Class Nine'),
    (10, 'Class Ten'),
]

SUBJECT_CHOICES = [
    ('bangla1', 'Bangla 1st Paper'),
    ('bangla2', 'Bangla 2nd Paper'),
    ('english1', 'English 1st Paper'),
    ('enlish2', 'English 2nd Paper'),
    ('math', 'Math'),
    ('religion', 'Religion'),
    ('ict', 'ICT'),
    ('physics', 'Physics'),
    ('chemistry', 'Chemistry'),
    ('biology', 'Biology'),
    ('highermath', 'Higher Math'),
    ('accounting', 'Accounting'),
    ('finance', 'Finance'),
    ('business', 'Business Entrepreneurship'),
    ('agriculture', 'Agricultural Studies'),
    ('gscinece', 'General Science'),
    ('bgs', 'Bangladesh and Global Studies'),
]

CHAPTERS_CHOICES = [
    (1, 'Chapter One'),
    (2, 'Chapter Two'),
    (3, 'Chapter Three'),
    (4, 'Chapter Four'),
    (5, 'Chapter Five'),
    (6, 'Chapter Six'),
    (7, 'Chapter Seven'),
    (8, 'Chapter Eight'),
    (9, 'Chapter Nine'),
    (10, 'Chapter Ten'),
]


POINT_CHOICES = [
    (5, 'Five Point'),
    (10, 'Ten Point'),
    (20, 'Twenty Point'),
    (50, 'Fifty Point'),
    (100, 'Hundred Point'),
]


class questions(models.Model):
    classes = models.IntegerField(choices=CLASSSS_CHOICES, default=None, null=True)
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=100, default=None, null=True)
    chapter = models.IntegerField(choices=CHAPTERS_CHOICES, default=None, null=True)
    scenario = models.TextField(max_length=3000, blank=True)
    ques_img = models.ImageField(blank=True, null=True)
    q_a = models.CharField(max_length=300, blank=True)
    q_b = models.CharField(max_length=300, blank=True)
    q_c = models.CharField(max_length=300, blank=True)
    q_d = models.CharField(max_length=300, blank=True)


class usercanvas(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    scenario = models.TextField(max_length=3000, blank=True)
    ques_img = models.ImageField(blank=True, null=True)
    q_a = models.CharField(max_length=300, blank=True)
    q_b = models.CharField(max_length=300, blank=True)
    q_c = models.CharField(max_length=300, blank=True)
    q_d = models.CharField(max_length=300, blank=True)


class selectiveQuestion(models.Model):
    classes = models.IntegerField(choices=CLASSSS_CHOICES, default=None, null=True)
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=100, default=None, null=True)
    chapter = models.IntegerField(choices=CHAPTERS_CHOICES, default=None, null=True)
    scenario = models.TextField(max_length=3000, blank=True)
    ques_img = models.ImageField(blank=True, null=True)
    q_a = models.CharField(max_length=300, blank=True)
    q_b = models.CharField(max_length=300, blank=True)
    q_c = models.CharField(max_length=300, blank=True)
    q_d = models.CharField(max_length=300, blank=True)


class usercanvasSelective(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    scenario = models.TextField(max_length=3000, blank=True)
    ques_img = models.ImageField(blank=True, null=True)
    q_a = models.CharField(max_length=300, blank=True)
    q_b = models.CharField(max_length=300, blank=True)
    q_c = models.CharField(max_length=300, blank=True)
    q_d = models.CharField(max_length=300, blank=True)


class userInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100, blank=True)
    point = models.IntegerField(default=0)


class paymentInformation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    package = models.IntegerField(choices=POINT_CHOICES, default=None, null=True)
    trxID = models.CharField(max_length=100, blank=True)


class userProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=300, null=True)
    user_phone = models.CharField(max_length=20, null=True)
    user_address = models.CharField(max_length=20, null=True)
    date = models.DateTimeField(auto_now_add=True)
    bio = models.CharField(max_length=300, null=True)
    user_image = models.ImageField(blank=True, null=True, upload_to='media', default='user.png')
