# Generated by Django 5.0.3 on 2024-04-17 16:16

import cpf_field.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.PositiveIntegerField(unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15)),
                ('cpf', cpf_field.models.CPFField(default='', max_length=14, verbose_name='cpf')),
                ('service', models.CharField(default='doctor', max_length=255)),
                ('price', models.FloatField(default=100.0)),
                ('bio', models.CharField(default='', max_length=255)),
                ('is_online', models.BooleanField(default=False)),
                ('address', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Nutritionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.PositiveIntegerField(unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('cpf', cpf_field.models.CPFField(default='', max_length=14, verbose_name='cpf')),
                ('service', models.CharField(max_length=255)),
                ('price', models.FloatField(default=100.0)),
                ('is_online', models.BooleanField(default=1)),
                ('bio', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'nutritionist',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15)),
                ('document', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('weight', models.PositiveIntegerField(blank=True, null=True)),
                ('bmi', models.PositiveIntegerField(blank=True, null=True)),
                ('history', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.PositiveIntegerField(unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=15)),
                ('cpf', cpf_field.models.CPFField(default='', max_length=14, verbose_name='cpf')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('service', models.CharField(default='doctor', max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_online', models.BooleanField(default=1)),
                ('bio', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 'personal',
            },
        ),
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('weight', models.PositiveBigIntegerField(max_length=255)),
                ('imc', models.PositiveIntegerField(max_length=255)),
                ('activity', models.CharField(max_length=255)),
                ('appetite', models.CharField(max_length=255)),
                ('chewing', models.CharField(max_length=255)),
                ('intestine', models.CharField(max_length=255)),
                ('sleep', models.CharField(max_length=255)),
                ('comments', models.CharField(max_length=255)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evolution', to='personal.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='evaluation/')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to='personal.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='diet/')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diet', to='personal.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=120)),
                ('professional_name', models.CharField(max_length=120)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('is_online', models.BooleanField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, choices=[('Cancelado', 'Cancelado'), ('Pendente', 'Pendente'), ('Confirmado', 'Confirmado')], max_length=20, null=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='personal.patient')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='personal.personal')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='training/')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Training', to='personal.patient')),
            ],
        ),
    ]
