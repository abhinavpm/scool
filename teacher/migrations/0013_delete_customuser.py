# Generated by Django 4.2.5 on 2023-09-11 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0012_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]