import django_filters
from .models import *


class PatientFilter(django_filters.FilterSet):

    class Meta:
        model = Patient
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'birth_date': ['icontains'],
            'birth_num': ['icontains'],
        }


class DoctorFilter(django_filters.FilterSet):

    class Meta:
        model = Doctor
        fields = {
            'user__first_name': ['icontains'],
            'user__last_name': ['icontains'],
            'room__id': ['icontains'],
            'room__department__name': ['icontains'],
        }


class NurseFilter(django_filters.FilterSet):

    class Meta:
        model = Nurse
        fields = {
            'user__first_name': ['icontains'],
            'user__last_name': ['icontains'],
            'room__id': ['icontains'],
            'room__department__name': ['icontains'],
        }


class VisitFilter(django_filters.FilterSet):

    class Meta:
        model = Visit
        fields = {
            'patient__first_name': ['icontains'],
            'patient__last_name': ['icontains'],
            'room__id': ['icontains'],
            'room__department__name': ['icontains'],
        }


class RoomFilter(django_filters.FilterSet):

    class Meta:
        model = Room
        fields = {
            'room_type__id': ['icontains'],
            'department__name': ['icontains'],
        }
