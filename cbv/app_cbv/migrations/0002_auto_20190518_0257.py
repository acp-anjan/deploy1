# Generated by Django 2.2 on 2019-05-18 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_cbv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientquery',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_query', to='app_cbv.Hospital'),
        ),
    ]
