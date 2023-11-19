# Generated by Django 4.2.5 on 2023-09-11 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0014_zero'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zero',
            options={},
        ),
        migrations.AlterModelManagers(
            name='zero',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='zero',
            name='username',
        ),
        migrations.AlterField(
            model_name='zero',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='zero',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='zero',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='zero',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='zero',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='zero',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
