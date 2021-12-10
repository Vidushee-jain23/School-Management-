# Generated by Django 3.2.6 on 2021-10-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=20)),
                ('dob', models.DateField()),
                ('subject', models.CharField(max_length=50)),
                ('mobileNo', models.IntegerField()),
                ('emailId', models.EmailField(max_length=50)),
                ('qualification', models.CharField(max_length=80)),
                ('experience', models.CharField(max_length=150)),
            ],
        ),
    ]