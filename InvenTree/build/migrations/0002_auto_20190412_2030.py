# Generated by Django 2.2 on 2019-04-12 10:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='part',
            field=models.ForeignKey(limit_choices_to={'buildable': True}, on_delete=django.db.models.deletion.CASCADE, related_name='builds', to='part.Part'),
        ),
        migrations.AlterField(
            model_name='build',
            name='status',
            field=models.PositiveIntegerField(choices=[(10, 'Pending'), (20, 'Holding'), (30, 'Cancelled'), (40, 'Complete')], default=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
