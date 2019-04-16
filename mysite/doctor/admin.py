from django.contrib import admin

# Register your models here.
from .models import Doctor, Nurse, Department, RoomTypes, Room, Patient
from .models import Drugs, Treatments, Diseases, Visit

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
