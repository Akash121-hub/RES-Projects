# Generated by Django 3.2 on 2023-03-14 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_employees_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.post'),
        ),
    ]
