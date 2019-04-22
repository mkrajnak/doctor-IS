from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .tables import *
from .filters import *
from .decorators import *


def index(request):
    return render(request, 'index.html', None)


@method_decorator([login_required, nurse_required], name='dispatch')
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


@method_decorator([login_required, receptionist_required], name='dispatch')
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


@method_decorator([login_required, receptionist_required], name='dispatch')
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


@method_decorator([login_required, nurse_required], name='dispatch')
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

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)

        if not (self.request.user.is_anonymous or self.request.user.is_superuser):
            if self.request.user.is_doctor:
                # show only patients from doctor's department
                queryset = queryset.filter(room__department=self.request.user.doctor.room.department)
            elif self.request.user.is_nurse:
                # show only patients from nurse's department
                queryset = queryset.filter(room__department=self.request.user.nurse.room.department)

        return queryset


@method_decorator([login_required, receptionist_required], name='dispatch')
class ReceptionVisitListView(SingleTableMixin, FilterView):
    table_class = VisitTablePartial
    model = Visit
    template_name = 'table_template.html'

    filterset_class = VisitFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Visit filter"
        context['called_from'] = self.request.path.split('/')[1]
        return context


@method_decorator([login_required, receptionist_required], name='dispatch')
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


@login_required
@receptionist_required
def reception_page(request):
    return render(request, 'reception.html', None)


@login_required
@nurse_required
def nurse_page(request):
    return render(request, 'nurse.html', None)


@login_required
@doctor_required
def doctor_page(request):
    return render(request, 'doctor.html', None)


@login_required
@admin_required
def admin_page(request):
    return render(request, 'admin.html', None)


@login_required
@admin_required
def go_back(request):
    return redirect(request.path.split('/')[1])


@login_required
@admin_required
def add_insurance(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)
    else:
        form = InsuranceForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_insurance/',
        'title': 'Insurance Company',
        'called_from': request.path.split('/')[1],
    })


@login_required
@admin_required
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)
    else:
        form = DepartmentForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_department/',
        'title': 'Department',
        'called_from': request.path.split('/')[1],
    })


@login_required
@admin_required
def add_room_type(request):
    if request.method == 'POST':
        form = RoomTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)

    else:
        form = RoomTypeForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_room_type/',
        'title': 'Room type',
        'called_from': request.path.split('/')[1],
    })


@login_required
@admin_required
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)
    else:
        form = RoomForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_room/',
        'title': 'Room',
        'called_from': request.path.split('/')[1],
    })


@login_required
@admin_required
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
            return go_back(request)
    else:
        form = DoctorForm()
        userform = UserForm()

    return render(request, 'add_form.html', {
        'userform': userform,
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_doctor/',
        'title': 'Doctor',
        'called_from': request.path.split('/')[1],
    })


@login_required
@admin_required
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

            return go_back(request)
    else:
        form = NurseForm()
        userform = UserForm()

    return render(request, 'add_form.html', {
        'userform': userform,
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_nurse/',
        'title': 'Nurse',
        'called_from': request.path.split('/')[1],
    })


@login_required
@admin_required
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

            return go_back(request)
    else:
        form = ReceptionistForm()
        userform = UserForm()

    return render(request, 'add_form.html', {
        'userform': userform,
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_receptionist/',
        'title': 'Receptionist',
        'called_from': request.path.split('/')[1],
    })


@login_required
@nurse_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)
    else:
        form = PatientForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_patient/',
        'title': 'Patient',
        'called_from': request.path.split('/')[1],
    })


@login_required
@doctor_required
def add_drugs(request):
    if request.method == 'POST':
        form = DrugsForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)
    else:
        form = DrugsForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_drugs/',
        'title': 'Drug',
        'called_from': request.path.split('/')[1],
    })


@login_required
@doctor_required
def add_treatments(request):
    if request.method == 'POST':
        form = TreatmentsForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)
    else:
        form = TreatmentsForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_treatments/',
        'title': 'Treatment',
        'called_from': request.path.split('/')[1],
    })


@login_required
@doctor_required
def add_diseases(request):
    if request.method == 'POST':
        form = DiseasesForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)
    else:
        form = DiseasesForm()

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_diseases/',
        'title': 'Disease',
        'called_from': request.path.split('/')[1],
    })


def get_room(request):
    try:
        if request.user.is_doctor:
            return Doctor.objects.get(user=request.user).room
        else:
            return Nurse.objects.get(user=request.user).room
    except Exception:
        return ''


def get_doctor(request):
    try:
        if request.user.is_doctor:
            return Doctor.objects.get(user=request.user)
        else:
            room = Nurse.objects.get(user=request.user).room
            return Doctor.objects.get(room=room)
    except Exception:
        return ''


@login_required
@nurse_required
def add_visits(request):
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            form.save()
            return go_back(request)
    else:
        form = VisitForm(initial={
        } if request.user.is_superuser else {
            'room': get_room(request),
            'doctor': get_doctor(request),
        })

    return render(request, 'add_form.html', {
        'form': form,
        'submit': '/' + request.path.split('/')[1] + '/add_visits/',
        'title': 'Visit',
        'called_from': request.path.split('/')[1],
    })
