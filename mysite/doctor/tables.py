import django_tables2 as tables
from .models import *


class PatientTable(tables.Table):
    class Meta:
        model = Patient


class DoctorTable(tables.Table):
    class Meta:
        model = Doctor


class NurseTable(tables.Table):
    class Meta:
        model = Nurse


class VisitTable(tables.Table):
    class Meta:
        model = Visit


class RoomTable(tables.Table):
    class Meta:
        model = Room
