from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Department)
admin.site.register(RoomTypes)
admin.site.register(Room)
admin.site.register(Patient)
admin.site.register(Drugs)
admin.site.register(Treatments)
admin.site.register(Diseases)
admin.site.register(Visit)
