import django_filters
from .models import *


class PatientFilter(django_filters.FilterSet):

    class Meta:
        model = Patient
        fields = {
            'insurance_num': ['icontains'],
        }
