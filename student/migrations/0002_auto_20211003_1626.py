# Generated by Django 3.2.6 on 2021-10-03 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='fatherMobileNo',
            new_name='mobileNo',
        ),
        migrations.RemoveField(
            model_name='studentinfo',
            name='motherMobileNo',
        ),
    ]
