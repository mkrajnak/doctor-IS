import django_tables2 as tables
from .models import *


class PatientTable(tables.Table):
    class Meta:
        model = Patient
