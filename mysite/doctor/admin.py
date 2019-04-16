from django.contrib import admin

# Register your models here.
from .models import Doctor, Nurse

admin.site.register(Doctor)
admin.site.register(Nurse)
