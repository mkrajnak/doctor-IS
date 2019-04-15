from django.db import models


class Department(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Department name", max_length=30)


class RoomTypes(models.Model):
    """
    Description: Model Description
    """
    id = models.CharField("Room type", max_length=10, primary_key=True)


class Room(models.Model):
    """
    Description: Model Description
    """
    id = models.CharField("Room number", max_length=10, primary_key=True)
    capacity = models.IntegerField()
    room_type = models.ForeignKey(RoomTypes, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Doctor(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField("Doctor's first name", max_length=50)
    last_name = models.CharField("Doctor's last name", max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Nurse(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField("Nurse's first name", max_length=50)
    last_name = models.CharField("Nurse's last name", max_length=50)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


class Patient(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    insurance_num = models.CharField("Insurance number", max_length=30)
    first_name = models.CharField("Nurse's first name", max_length=50)
    last_name = models.CharField("Nurse's last name", max_length=50)


class Drugs(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Drug name", max_length=30)
    description = models.CharField("Drug description", max_length=300)
    price = models.DecimalField(verbose_name="Drug's price", max_digits=10, decimal_places=2)
    pbi = models.DecimalField(verbose_name="Amount paid by insurance", max_digits=10, decimal_places=2)


class Treatments(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Treatment name", max_length=30)
    description = models.CharField("Treatment description", max_length=300)


class Diseases(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Disease name", max_length=30)
    description = models.CharField("Disease description", max_length=300)


class Visit(models.Model):
    """
    Description: Model Description
    """
    id = models.AutoField(primary_key=True)
    treatment = models.ForeignKey(Treatments, on_delete=models.CASCADE)
    disease = models.ManyToManyField(Diseases)
    drugs = models.ManyToManyField(Drugs)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
