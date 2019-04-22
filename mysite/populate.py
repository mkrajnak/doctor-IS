# -*- coding: utf-8 -*-
import django
import os


DEPS = [
    'Accident and emergency', 'Anaesthetics', 'Breast screening',
    'Cardiology', 'Chaplaincy', 'Critical care', 'Diagnostic imaging',
    'Discharge lounge', 'Ear nose and throat', 'Elderly services',
    'Gastroenterology', 'General surgery', 'Gynaecology', 'Haematology',
    'Maternity departments', 'Microbiology', 'Neonatal unit', 'Nephrology',
    'Neurology', 'Nutrition and dietetics', 'Orthopaedics', 'Rheumatology',
    'Occupational therapy', 'Oncology', 'Ophthalmology', 'Pharmacy',
    'Obstetrics and gynaecology', 'Physiotherapy', 'Radiotherapy'
    ]
ROOMTYPES = [
    'Maintanance', 'Office', 'Storage Room', 'Czech Insurance Company',
    'Ordination Room', 'Surgery Room', 'Room']
INSURANCE = ['Generalli', 'Axa', 'Union', 'Czech Insurance Company']
DRUGS = [
    [
        'Tobacco',
        'Nicotine addiction may not appear as harmful as many other addictions.'
    ],
    [
        'Alcohol',
        'The social acceptance of drinking can make alcohol addiction hard to spot.'
    ],
    [
        'Marijuana',
        'he legalization of marijuana in some states has made the drug’s use more socially acceptable.'
    ],
    [
        'Painkillers',
        'Drugs like codeine, Vicodin and Oxycontin are commonly prescribed to treat pain.'
    ],
    [
        'Cocaine',
        'Rates of cocaine addiction in the United States are dropping.'
    ],
    [
        'Heroin',
        'Heroin’s severe withdrawal symptoms make beating a heroin addiction a difficult task.'
    ],
    [
        'Benzodiazepines',
        '“Benzos” — such as Valium, Xanax, Diazepam and Klonopin — are prescribed as mood-regulating drugs to manage conditions like anxiety and stress. '
    ],
]
TREATMENTS = [
    [
        'Transesophageal echocardiography',
        'In simple terms, this procedure takes pictures of your heart using ultrasound via a tube inserted into your oesophagus. A doctor might use this instead of doing an electrocardiogram, but research suggests any extra detail it might produce isn\'t worth the risks of being sedated.'
    ],
    [
        'Computed tomography pulmonary angiography',
        'A diagnostic test that images the pulmonary arteries in patients with respiratory symptoms using a CT scan. It isn\'t invasive, and is highly sensitive, but hits the patient with a dose of radiation. The wait for this test is likely to result in delays that raise the risk of complications developing.'
    ],
    [
        'Computed tomography in any patients with respiratory symptoms',
        'Any kind of CT scan on a patient with non-life threatening respiratory symptoms, according to the study, does little to improve the patient\'s outcome. Worse still, these scans raise risks of false positives, where the test indicates a non-existent pathology.'
    ],
    [
        'Carotid artery ultrasonography and stenting',
        'Carotid ultrasounds are done to test the width of arteries at the neck, which could help indicate risk of stroke.'
    ],
    [
        'Aggressive management of prostate cancer',
        'Prostate cancer is another condition that can be treated easily if found early.'
    ],
    [
        'Supplemental oxygen for patients with chronic obstructive pulmonary disease',
        'Giving more oxygen to patients with the lung illness COPD didn\'t help their lungs work better or improve their wellbeing. But it can cause them to retain carbon dioxide. Which isn\'t good.'
    ],
    [
        'Surgery for meniscal cartilage tears',
        'Ripping the C-shaped shock-absorbing discs of cartilage inside your knee is no laughing matter. But going to the trouble of repairing it surgically was found to have few benefits that couldn\'t be achieved through conservative management and rehabilitation.'
    ],
]
DISEASES = [
    [
        'Acne',
        'Acne vulgaris is a long term skin condition characterized by areas of blackheads, whiteheads, pimples, greasy skin, and possibly scarring.'
    ],
    [
        'Allergy',
        'An allergy is a hypersensitivity disorder of the immune system. .'
    ],
    [
        'Antisocial personality disorder',
        'Antisocial personality disorder is characterized by a pervasive pattern of disregard for, or violation of, the rights of others. '
    ],
    [
        'Attention deficit hyperactivity disorder',
        'Attention deficit hyperactivity disorder is a developmental neuropsychiatric disorder in which there are significant problems with executive functions that cause attention deficits'
    ],
    [
        'Altitude sickness',
        'Altitude sickness—also known as acute mountain sickness, altitude illness, hypobaropathy, "the altitude bends", or soroche—is a pathological effect of high altitude on humans'
    ],
    [
        'Alzheimer\'s disease',
        'Alzheimer\'s Disease is a progressive, neurodegenerative disease characterized by loss of function and death of nerve cells in several areas of the brain leading to loss of cognitive function'
    ],
    [
        'Asperger syndrome',
        'Asperger syndrome, also known as Asperger\'s syndrome, Asperger disorder or simply Asperger\'s, is an autism spectrum disorder that is characterized by significant difficulties in social.'
    ],
]


def cleanup():
    Visit.objects.all().delete()
    Patient.objects.all().delete()
    Insurance.objects.all().delete()
    Department.objects.all().delete()
    RoomTypes.objects.all().delete()
    Room.objects.all().delete()
    Treatments.objects.all().delete()
    Diseases.objects.all().delete()
    Drugs.objects.all().delete()
    Doctor.objects.all().delete()
    Nurse.objects.all().delete()
    User.objects.all().delete()


def print_all():
    print('Visits:')
    print(Visit.objects.all())
    print('Patients:')
    print(Patient.objects.all())
    print('Insurances:')
    print(Insurance.objects.all())
    print('Departments:')
    print(Department.objects.all())
    print('RoomTypes:')
    print(RoomTypes.objects.all())
    print('Rooms:')
    print(Room.objects.all())
    print('Drugs:')
    print(Drugs.objects.all())
    print('Treatmentss:')
    print(Treatments.objects.all())
    print('Diseasess:')
    print(Diseases.objects.all())
    print('Doctors:')
    print(Doctor.objects.all())
    print('Nurses:')
    print(Nurse.objects.all())
    print('Users:')
    print(User.objects.all())


def populate_departments():
    for d in DEPS:
        Department.objects.create(name=d)


def populate_insurance():
    for c in INSURANCE:
        Insurance.objects.create(name=c)


def populate_room_types():
    for t in ROOMTYPES:
        RoomTypes.objects.create(id=t)


def populate_rooms():
    for i in range(100):
        Room.objects.create(
            id=f'Room {i}',
            capacity=2,
            room_type=RoomTypes.objects.get(id=ROOMTYPES[i % len(ROOMTYPES)]),
            department=Department.objects.get(name=DEPS[i % len(DEPS)])
            )


def populate_drugs():
    import random
    for drug in DRUGS:
        dolla = random.uniform(10.5,100.5)
        Drugs.objects.create(
            name=drug[0],
            description=drug[1],
            price=dolla,
            pbi=dolla - 10
            )


def populate_treatments():
    for t in TREATMENTS:
        Treatments.objects.create(
            name=t[0],
            description=t[1]
            )


def populate_diseases():
    for d in DISEASES:
        Diseases.objects.create(
            name=d[0],
            description=d[1]
            )


def add_patient(name, surname, birth_date, birth_num, insurance):
    Patient.objects.create(
        first_name=name,
        last_name=surname,
        birth_date=birth_date,
        birth_num=birth_num,
        insurance=Insurance.objects.get(name=insurance),
    )


def populate_patients():
    i = 1234567890
    add_patient(
        'Radovan', 'Koza', "1999-09-01T13:20:30+01:00", str(i), 'Generalli')
    i += 1
    add_patient(
        'Dominik', 'Baran', "1979-09-01T13:20:30+01:00", str(i), 'Union')
    i += 1
    add_patient(
        'Jozef', 'Vydrel', "1989-09-01T13:20:30+01:00", str(i), 'Generalli')
    i += 1
    add_patient(
        'Adam', 'Lata', "2009-09-01T13:20:30+01:00", str(i), 'Axa')


def add_user(username, name, surname, passwd, mail, doctor, nurse, reception):
    # UserModel = get_user_model()
    return User.objects.create_user(
        username=username,
        first_name=name,
        last_name=surname,
        password=passwd,
        email=mail,
        is_doctor=doctor,
        is_nurse=nurse,
        is_receptionist=reception
    )


def add_doctor(username, name, surname, passwd, mail, room):
    user = add_user(username, name, surname, passwd, mail, True, True, True)
    Doctor.objects.create(
        user=user,
        room=Room.objects.get(id=room)
    )


def add_nurse(username, name, surname, passwd, mail, room):
    user = add_user(username, name, surname, passwd, mail, False, True, True)
    Nurse.objects.create(
        user=user,
        room=Room.objects.get(id=room)
    )


def add_receptionist(username, name, surname, passwd, mail):
    user = add_user(username, name, surname, passwd, mail, False, False, True)
    Receptionist.objects.create(user=user)


def populate_staff():
    add_doctor('tdudlak', 'Tibor', 'Dudlak', '2451', 'tibi@mendelu.hu', 'Room 1')
    add_doctor('kgruberova', 'Katarina', 'Gruberova', '2451', 'Kikgr@dmail.de', 'Room 76')
    add_doctor('petersm', 'Samuel', 'Peter', '2451', 'speter@mahalo.hu', 'Room 29')


    add_nurse('jdoe', 'Jane', 'Dudlak', '2451', 'jane@mendelu.hu', 'Room 1')
    add_nurse('annkr', 'Anna', 'Kratomila', '2451', 'Ann@dmail.de', 'Room 76')
    add_nurse('efiala', 'Ester', 'Fialkova', '2451', 'esther@dmail.de', 'Room 29')


    add_receptionist('jsmith', 'Jenny', 'Smith', '2451', 'jenny@mendelu.hu')
    add_receptionist('dla', 'Dimitri', 'Laszskow', '2451', 'dimml@mahalo.hu')
    add_receptionist('reception', 'Tamara', 'Suchankova', '2451', 'tamarSuch@dmail.de')


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from doctor.models import *

    cleanup()

    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    populate_departments()
    populate_insurance()
    populate_room_types()
    populate_rooms()
    populate_drugs()
    populate_treatments()
    populate_diseases()
    populate_patients()
    populate_staff()

    print_all()
