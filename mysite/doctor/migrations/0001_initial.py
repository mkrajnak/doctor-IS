# Generated by Django 2.2 on 2019-04-15 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Department name')),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Disease name')),
                ('description', models.CharField(max_length=300, verbose_name='Disease description')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name="Doctor's first name")),
                ('last_name', models.CharField(max_length=50, verbose_name="Doctor's last name")),
            ],
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Drug name')),
                ('description', models.CharField(max_length=300, verbose_name='Drug description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Drug's price")),
                ('pbi', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount paid by insurance')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('insurance_num', models.CharField(max_length=30, verbose_name='Insurance number')),
                ('first_name', models.CharField(max_length=50, verbose_name="Nurse's first name")),
                ('last_name', models.CharField(max_length=50, verbose_name="Nurse's last name")),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Room number')),
                ('capacity', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Department')),
            ],
        ),
        migrations.CreateModel(
            name='RoomTypes',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Room type')),
            ],
        ),
        migrations.CreateModel(
            name='Treatments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='Treatment name')),
                ('description', models.CharField(max_length=300, verbose_name='Treatment description')),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('disease', models.ManyToManyField(to='doctor.Diseases')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.Doctor')),
                ('drugs', models.ManyToManyField(to='doctor.Drugs')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.Patient')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Room')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Treatments')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.RoomTypes'),
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name="Nurse's first name")),
                ('last_name', models.CharField(max_length=50, verbose_name="Nurse's last name")),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Room')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Room'),
        ),
    ]