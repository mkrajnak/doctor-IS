from django.urls import path
from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('doctor/', views.doctor_page, name='doctor'),
    path('reception/', views.reception_page, name='reception'),
    path('nurse/', views.nurse_page, name='nurse'),
    path('my_admin/', views.admin_page, name='my_admin'),

    path('my_admin/add_department/', views.add_department, name='add_department_admin'),
    path('my_admin/add_insurance/', views.add_insurance, name='add_insurance_admin'),
    path('my_admin/add_room_type/', views.add_room_type, name='add_room_type_admin'),
    path('my_admin/add_room/', views.add_room, name='add_room_admin'),
    path('my_admin/add_doctor/', views.add_doctor, name='add_doctor_admin'),
    path('my_admin/add_nurse/', views.add_nurse, name='add_nurse_admin'),
    path('my_admin/add_receptionist/', views.add_receptionist, name='add_receptionist_admin'),
    path('my_admin/add_patient/', views.add_patient, name='add_patient_admin'),
    path('my_admin/add_drugs/', views.add_drugs, name='add_drugs_admin'),
    path('my_admin/add_treatments/', views.add_treatments, name='add_treatments_admin'),
    path('my_admin/add_visits/', views.add_visits, name='add_visits_admin'),
    path('my_admin/add_diseases/', views.add_diseases, name='add_diseases_admin'),
    path('doctor/add_patient/', views.add_patient, name='add_patient_doc'),
    path('doctor/add_drugs/', views.add_drugs, name='add_drugs_doc'),
    path('doctor/add_treatments/', views.add_treatments, name='add_treatments_doc'),
    path('doctor/add_visits/', views.add_visits, name='add_visits_doc'),
    path('nurse/add_patient/', views.add_patient, name='add_patient_nurse'),
    path('nurse/add_visits/', views.add_visits, name='add_visits_nurse'),

    path('doctor/patient_filter/', views.FilteredPatientListView.as_view(), name='show_patients_doc'),
    path('nurse/patient_filter/', views.FilteredPatientListView.as_view(), name='show_patients_nurse'),
    path('doctor/visit_filter/', views.FilteredVisitListView.as_view(), name='show_visits_doc'),
    path('nurse/visit_filter/', views.FilteredVisitListView.as_view(), name='show_visits_nurse'),
    path('reception/visit_filter/', views.ReceptionVisitListView.as_view(), name='show_visits_rec'),
    path('reception/doctor_filter/', views.FilteredDoctorListView.as_view(), name='show_doctors_rec'),
    path('reception/nurse_filter/', views.FilteredNurseListView.as_view(), name='show_nurses_rec'),
    path('reception/rooms/', views.RoomsListView.as_view(), name='show_by_dept'),
]
