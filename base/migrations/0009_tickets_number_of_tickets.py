# Generated by Django 3.2.8 on 2022-07-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='number_of_tickets',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
