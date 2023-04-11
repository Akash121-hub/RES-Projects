# Generated by Django 3.2 on 2023-03-13 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0012_alter_employees_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='posts',
        ),
        migrations.AddField(
            model_name='post',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]