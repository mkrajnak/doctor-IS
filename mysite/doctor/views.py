from django.shortcuts import render
from .models import *
from .forms import *
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .tables import *
from .filters import *
from django.views.generic.list import ListView

def index(request):
    return render(request, 'index.html', None)


class FilteredPatientListView(SingleTableMixin, FilterView):
    table_class = PatientTable
    model = Patient
    template_name = 'table_template.html'

    filterset_class = PatientFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Patient filter"
        context['called_from'] = self.request.path.split('/')[1]
        return context


class FilteredDoctorListView(SingleTableMixin, FilterView):
    table_class = DoctorTable
    model = Doctor
    template_name = 'table_template.html'

    filterset_class = DoctorFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Doctor filter"
        context['called_from'] = self.request.path.split('/')[1]
        return context


class FilteredNurseListView(SingleTableMixin, FilterView):
    table_class = NurseTable
    model = Nurse
    template_name = 'table_template.html'

    filterset_class = NurseFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Nurse filter"
        context['called_from'] = self.request.path.split('/')[1]
        return context


class FilteredVisitListView(SingleTableMixin, FilterView):
    table_class = VisitTable
    model = Visit
    template_name = 'table_template.html'

    filterset_class = VisitFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Visit filter"
        context['called_from'] = self.request.path.split('/')[1]
        return context


class RoomsListView(SingleTableMixin, FilterView):
    table_class = RoomTable
    model = Room
    template_name = 'table_template.html'

    filterset_class = RoomFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Rooms"
        context['called_from'] = self.request.path.split('/')[1]
        return context


def reception_page(request):
    return render(request, 'reception.html', None)


def nurse_page(request):
    return render(request, 'nurse.html', None)


def doctor_page(request):
    return render(request, 'doctor.html', None)


def admin_page(request):
    return render(request, 'admin.html', None)


def get_departments(request):
    return render(request, 'doctors/index.html', {
        'objects': Department.objects.all(),
    })


def get_insurance(request):
    return render(request, 'doctors/index.html', {
        'objects': Insurance.objects.all(),
    })


def get_room_types(request):
    return render(request, 'doctors/index.html', {
        'objects': RoomTypes.objects.all(),
    })


def get_rooms(request):
    return render(request, 'doctors/index.html', {
        'objects': Room.objects.all(),
    })


def get_doctors(request):
    return render(request, 'doctors/index.html', {
        'objects': Doctor.objects.all(),
    })


def get_nurses(request):
    return render(request, 'doctors/index.html', {
        'objects': Nurse.objects.all(),
    })


def get_receptionists(request):
    return render(request, 'doctors/index.html', {
        'objects': Receptionist.objects.all(),
    })


def get_patients(request):
    return render(request, 'doctors/index.html', {
        'objects': Patient.objects.all(),
    })


def get_drugs(request):
    return render(request, 'doctors/index.html', {
        'objects': Drugs.objects.all(),
    })


def get_treatments(request):
    return render(request, 'doctors/index.html', {
        'objects': Treatments.objects.all(),
    })


def get_diseases(request):
    return render(request, 'doctors/index.html', {
        'objects': Diseases.objects.all(),
    })


def get_visits(request):
    return render(request, 'doctors/index.html', {
        'objects': Visit.objects.all(),
    })


def add_insurance(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            return get_insurance(request)
    else:
        form = InsuranceForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_insurance/',
        'title': 'Insurance Company',
        'called_from': request.path.split('/')[1],
    })


def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return get_departments(request)
    else:
        form = DepartmentForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_department/',
        'title': 'Department',
        'called_from': request.path.split('/')[1],
    })


def add_room_type(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return get_room_types(request)

    else:
        form = RoomTypeForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_room_type/',
        'title': 'Room type',
        'called_from': request.path.split('/')[1],
    })


def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return get_rooms(request)
    else:
        form = RoomForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_room/',
        'title': 'Room',
        'called_from': request.path.split('/')[1],
    })


def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        userform = UserForm(request.POST)
        if form.is_valid() and userform.is_valid():
            user = userform.save()
            doctor = form.save(commit=False)
            doctor.user = User.objects.get(username=user.username)
            doctor.user.is_doctor = True
            doctor.user.set_password(user.password)
            doctor.user.save()
            doctor.save()
            return get_doctors(request)
    else:
        form = DoctorForm()
        userform = UserForm()

    return render(request, 'add_form.html', {
        'userform': userform,
        'form': form,
        'submit': '/add_doctor/',
        'title': 'Doctor',
        'called_from': request.path.split('/')[1],
        })


def add_nurse(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        userform = UserForm(request.POST)
        if form.is_valid() and userform.is_valid():
            user = userform.save()
            nurse = form.save(commit=False)
            nurse.user = User.objects.get(username=user.username)
            nurse.user.is_nurse = True
            nurse.user.set_password(user.password)
            nurse.user.save()
            nurse.save()

            return get_nurses(request)
    else:
        form = NurseForm()
        userform = UserForm()

    return render(request, 'add_form.html', {
        'userform': userform,
        'form': form,
        'submit': '/add_nurse/',
        'title': 'Nurse',
        'called_from': request.path.split('/')[1],
    })


def add_receptionist(request):
    if request.method == 'POST':
        form = ReceptionistForm(request.POST)
        userform = UserForm(request.POST)
        if form.is_valid() and userform.is_valid():
            user = userform.save()
            receptionist = form.save(commit=False)
            receptionist.user = User.objects.get(username=user.username)
            receptionist.user.is_receptionist = True
            receptionist.user.set_password(user.password)
            receptionist.user.save()
            receptionist.save()

            return get_receptionists(request)
    else:
        form = ReceptionistForm()
        userform = UserForm()

    return render(request, 'add_form.html', {
        'userform': userform,
        'form': form,
        'submit': '/add_receptionist/',
        'title': 'Receptionist',
        'called_from': request.path.split('/')[1],
    })


def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return get_patients(request)
    else:
        form = PatientForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_patient/',
        'title': 'Patient',
        'called_from': request.path.split('/')[1],
        })


def add_drugs(request):
    if request.method == 'POST':
        form = DrugsForm(request.POST)
        if form.is_valid():
            form.save()
            return get_drugs(request)
    else:
        form = DrugsForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_drugs/',
        'title': 'Drug',
        'called_from': request.path.split('/')[1],
    })


def add_treatments(request):
    if request.method == 'POST':
        form = TreatmentsForm(request.POST)
        if form.is_valid():
            form.save()
            return get_treatments(request)
    else:
        form = TreatmentsForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_treatments/',
        'title': 'Treatment',
        'called_from': request.path.split('/')[1],
    })


def add_diseases(request):
    if request.method == 'POST':
        form = DiseasesForm(request.POST)
        if form.is_valid():
            form.save()
            return get_diseases(request)
    else:
        form = DiseasesForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_diseases/',
        'title': 'Disease',
        'called_from': request.path.split('/')[1],
    })


def add_visits(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return get_visits(request)
    else:
        form = VisitForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/add_visits/',
        'title': 'Visit',
        'called_from': request.path.split('/')[1],
    })
