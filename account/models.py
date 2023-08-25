from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100) 
    userFullName = models.CharField(max_length=100)
    SEX_CHOICES = (
        ('MALE','man'),
        ('FEMALE','woman'),
        ('NONE','nochoice')
    )
    userSex = models.CharField(max_length=100, choices=SEX_CHOICES)
    userAge = models.IntegerField(default=0)
    userNation = CountryField(blank_label='Choose your nation')
    selfIntro = models.TextField()
    LANGUAGE_CHOICES = (
        ('eng', 'English'),
        ('kor', 'Korean'),
        ('fra', 'French'),
        ('jpn', 'Japanese'),
        ('zho', 'Chinese'),
        ('spa', 'Spanish'),
        ('deu', 'Deutsch'),  # 독일어
        ('rus', 'Russian'),  # 러시아어
        ('hin', 'Hindi'),  # 힌디어
        ('ara', 'Arabic'),  # 아랍어
    )

    language = MultiSelectField(max_length=100, choices=LANGUAGE_CHOICES)
    userUni = models.CharField(max_length=100)
    userSNS = models.URLField()