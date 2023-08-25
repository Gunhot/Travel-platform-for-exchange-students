from django.contrib import admin
from .models import User

# Register your models here.
from .models import *
admin.site.register(User)
