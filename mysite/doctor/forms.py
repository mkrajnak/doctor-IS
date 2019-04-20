from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


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

    def clean(self):
        cleaned_data = super(PatientForm, self).clean()
        insurance_num = cleaned_data.get("insurance_num")

        if not insurance_num.isdigit():
            msg = "Invalid format, e.g for 190419/0013 enter 1904190013"
            self.add_error('insurance_num', msg)
        if len(insurance_num) > 10 or len(insurance_num) < 10:
            self.add_error('insurance_num', 'Number must contain 10 digits')

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
