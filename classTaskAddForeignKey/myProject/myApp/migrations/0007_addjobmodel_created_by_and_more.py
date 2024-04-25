# Generated by Django 5.0.3 on 2024-04-25 06:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_addjobmodel_ownerofjobpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='addjobmodel',
            name='Created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='BloodGroup',
            field=models.CharField(choices=[('A+', 'A positive'), ('A-', 'A negative'), ('B+', 'B positive'), ('B-', 'B negative'), ('AB+', 'AB positive'), ('AB-', 'AB negative'), ('O+', 'O positive'), ('O-', 'O negative')], max_length=100, null=True),
        ),
    ]
