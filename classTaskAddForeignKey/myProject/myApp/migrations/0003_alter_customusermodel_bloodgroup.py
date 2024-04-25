# Generated by Django 5.0.4 on 2024-04-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_remove_customusermodel_displayname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='BloodGroup',
            field=models.CharField(choices=[('A+', 'A positive'), ('A-', 'A negative'), ('B+', 'B positive'), ('B-', 'B negative'), ('AB', 'AB positive'), ('AB-', 'AB negative'), ('O+', 'O positive'), ('O-', 'O negative')], max_length=100, null=True),
        ),
    ]