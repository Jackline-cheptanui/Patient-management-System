# Generated by Django 4.0.6 on 2022-07-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_rename_registration_date_patient_registration_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='First_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Registration_date',
            new_name='registration_date',
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=17, null=True),
        ),
    ]
