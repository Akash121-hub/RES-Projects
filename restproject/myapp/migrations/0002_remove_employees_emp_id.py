# Generated by Django 3.1.4 on 2021-03-22 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='emp_Id',
        ),
    ]
