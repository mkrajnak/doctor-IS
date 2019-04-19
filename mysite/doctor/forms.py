from django.forms import ModelForm
from .models import Doctor, RoomTypes, Room


class RoomTypeForm(ModelForm):
    class Meta:
        model = RoomTypes
        fields = '__all__'


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
