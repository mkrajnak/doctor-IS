from django.contrib.admin import widgets
from django import forms
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomTypes
        fields = '__all__'


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class DrugsForm(forms.ModelForm):
    class Meta:
        model = Drugs
        fields = '__all__'


class TreatmentsForm(forms.ModelForm):
    class Meta:
        model = Treatments
        fields = '__all__'


class DiseasesForm(forms.ModelForm):
    class Meta:
        model = Diseases
        fields = '__all__'


class VisitForm(forms.ModelForm):
    # SplitDateTimeWidget
    start_date = forms.DateField(widget=forms.SelectDateWidget)
    end_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Visit
        fields = '__all__'
