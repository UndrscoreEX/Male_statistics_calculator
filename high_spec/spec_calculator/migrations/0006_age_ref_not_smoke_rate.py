# Generated by Django 4.1.3 on 2022-12-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spec_calculator', '0005_rename_is_obese_age_ref_is_obese_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='age_ref',
            name='not_smoke_rate',
            field=models.FloatField(default=4),
            preserve_default=False,
        ),
    ]
