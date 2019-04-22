from django import forms
from django.utils import timezone
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        super().clean()
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            self.add_error('password2', 'Passwords are not matching')

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'email',
            'first_name',
            'last_name'
        ]


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class InsuranceForm(forms.ModelForm):
    class Meta:
        model = Insurance
        fields = '__all__'


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomTypes
        fields = '__all__'


class RoomForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['room_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['department'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Room
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields['room'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['user']


class NurseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NurseForm, self).__init__(*args, **kwargs)
        self.fields['room'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Nurse
        fields = '__all__'
        exclude = ['user']


class ReceptionistForm(forms.ModelForm):
    class Meta:
        model = Receptionist
        fields = '__all__'
        exclude = ['user']


class PatientForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['insurance'].widget.attrs.update({'class': 'form-control'})
        self.fields['birth_date'] = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super(PatientForm, self).clean()
        num = cleaned_data.get("birth_num")

        if not num.isdigit():
            msg = "Invalid format, e.g for 190419/0013 enter 1904190013"
            self.add_error('birth_num', msg)
        if len(num) > 10 or len(num) < 10:
            self.add_error('birth_num', 'Number must contain 10 digits')

    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ['user']


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

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        self.fields['patient'].widget.attrs.update({'class': 'form-control'})
        self.fields['disease'].widget.attrs.update({'class': 'form-control'})
        self.fields['treatment'].widget.attrs.update({'class': 'form-control'})
        self.fields['drugs'].widget.attrs.update({'class': 'form-control'})
        self.fields['room'].widget.attrs.update({'class': 'form-control'})
        self.fields['doctor'].widget.attrs.update({'class': 'form-control'})
        # Time widget -> 'type': 'datetime-local'
        self.fields['start_date'] = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))
        self.fields['end_date'] = forms.DateTimeField(
            widget=forms.widgets.DateTimeInput(attrs={'type': 'date'}))

    class Meta:
        model = Visit
        # Force render order
        fields = [
            'patient',
            'disease',
            'treatment',
            'drugs',
            'room',
            'doctor',
            'start_date',
            'end_date'
        ]
