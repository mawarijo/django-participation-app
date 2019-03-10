# Generated by Django 2.1.7 on 2019-03-10 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participation_app', '0006_auto_20190310_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='present',
            field=models.CharField(choices=[('AB', 'Absent'), ('TR', 'Tardy'), ('OT', 'On-Time')], default='AB', max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='year_in_school',
            field=models.CharField(choices=[('SR', 'Senior'), ('JR', 'Junior'), ('SO', 'Sophomore'), ('FR', 'Freshman')], default='FR', max_length=2),
        ),
    ]
