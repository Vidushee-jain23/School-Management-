# Generated by Django 3.2.6 on 2021-10-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_studentinfo_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='mobileNo',
            field=models.CharField(max_length=20),
        ),
    ]
