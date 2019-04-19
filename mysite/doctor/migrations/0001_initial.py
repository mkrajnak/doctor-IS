# Generated by Django 2.2 on 2019-04-19 23:22

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_doctor', models.BooleanField(default=False, verbose_name='doctor status')),
                ('is_nurse', models.BooleanField(default=False, verbose_name='nurse status')),
                ('is_receptionist', models.BooleanField(default=False, verbose_name='receptionist status')),
                ('is_patient', models.BooleanField(default=False, verbose_name='patient status')),
                ('first_name', models.CharField(max_length=50, verbose_name="Doctor's first name")),
                ('last_name', models.CharField(max_length=50, verbose_name="Doctor's last name")),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
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
            name='Doctor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('insurance_num', models.CharField(max_length=30, verbose_name='Insurance number')),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Room number')),
                ('capacity', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Department')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.RoomTypes')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[

                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('disease', models.ManyToManyField(to='doctor.Diseases')),
                ('drugs', models.ManyToManyField(to='doctor.Drugs')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Room')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Treatments')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Room')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Room'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('disease', models.ManyToManyField(to='doctor.Diseases')),
                ('drugs', models.ManyToManyField(to='doctor.Drugs')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Room')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Treatments')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctor.Patient')),
            ],
        ),
    ]
