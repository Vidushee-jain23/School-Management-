# Generated by Django 3.2.6 on 2021-10-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=10)),
                ('dob', models.DateField()),
                ('fatherName', models.CharField(max_length=50)),
                ('fatherOccupation', models.CharField(max_length=70)),
                ('fatherMobileNo', models.IntegerField()),
                ('motherName', models.CharField(max_length=50)),
                ('motherOccupation', models.CharField(max_length=70)),
                ('motherMobileNo', models.IntegerField()),
                ('address', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
            ],
        ),
    ]
