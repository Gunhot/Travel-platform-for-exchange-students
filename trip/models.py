from django.db import models
from account.models import *
from django.conf import settings

# Create your models here.
class trip(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(null =True, blank=True )
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    trip_intro = models.TextField() #여행 간략 소개
    trip_detail = models.TextField() #여행 계획
    leader = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='led_trips',
        null=True
    )
    trip_places = models.TextField() #여행 장소
    trip_accmdtn = models.TextField() #숙소 지역
    google_form = models.URLField(null=True, blank=True)

    REGION_CHOICES = (
        ('R1','서울권'),
        ('R2','경기/인천'),
        ('R3','강원권'),
        ('R4','충청권'),
        ('R5','전라권'),
        ('R6','경상권'),
        ('R7','제주도')
    )

    PERIOD_CHOICES = (
        ('P1','당일치기'),
        ('P2','3일 이내'),
        ('P3','일주일 이내'),
        ('P4','일주일 이상')
    )

    THEME_CHOICES = (
        ('T1','힐링'),
        ('T2','K-문화체험'),
        ('T3','유적지 탐방'),
        ('T4','식도락'),
        ('T5','패션쇼핑'),
    )
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    period = models.CharField(max_length=100, choices=PERIOD_CHOICES)
    theme = models.CharField(max_length=100, choices=THEME_CHOICES)
    

    estimated_cost = models.IntegerField()
#자기소개, 여행계획, 숙소지역, 장소