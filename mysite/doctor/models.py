from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class User(AbstractUser):
    is_doctor = models.BooleanField('doctor status', default=False)
    is_nurse = models.BooleanField('nurse status', default=False)
    is_receptionist = models.BooleanField('receptionist status', default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Department(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Department name", max_length=50)

    def __str__(self):
        return self.name


class Insurance(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Insurance Company Name", max_length=50)

    def __str__(self):
        return self.name


class RoomTypes(models.Model):
    """
    Description: Model Description
    """
    id = models.CharField("Room type", max_length=50, primary_key=True)

    def __str__(self):
        return self.id


class Room(models.Model):
    """
    Description: Model Description
    """
    id = models.CharField("Room number", max_length=10, primary_key=True)
    capacity = models.IntegerField()
    room_type = models.ForeignKey(RoomTypes, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}, {self.department.name}'


class Receptionist(models.Model):
    """docstring for Receptionist"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Doctor(models.Model):
    """
    Description: Model Description
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Nurse(models.Model):
    """
    Description: Model Description
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Patient(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField("Name", max_length=50)
    last_name = models.CharField("Surname", max_length=50)
    birth_date = models.DateTimeField()
    birth_num = models.CharField("Birth number", max_length=10, unique=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Drugs(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Drug name", max_length=50)
    description = models.CharField("Drug description", max_length=300)
    price = models.DecimalField(verbose_name="Drug's price", max_digits=10, decimal_places=2)
    pbi = models.DecimalField(verbose_name="Amount paid by insurance", max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.description}'


class Treatments(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Treatment name", max_length=150)
    description = models.CharField("Treatment description", max_length=600)

    def __str__(self):
        return f'{self.name}'


class Diseases(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Disease name", max_length=50)
    description = models.CharField("Disease description", max_length=300)

    def __str__(self):
        return f'{self.name}'


class Visit(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    treatment = models.ForeignKey(Treatments, on_delete=models.CASCADE)
    disease = models.ForeignKey(Diseases, on_delete=models.DO_NOTHING)
    drugs = models.ForeignKey(Drugs, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(default=now, blank=True)
    end_date = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.id} {self.patient.first_name} {self.patient.last_name}'
