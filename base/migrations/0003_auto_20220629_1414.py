# Generated by Django 3.2.8 on 2022-06-29 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_adminstrator_countrie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline_Companie',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=70, null=True, unique=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('countrie_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.countrie')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('departure_time', models.DateTimeField()),
                ('landing_time', models.DateTimeField()),
                ('remaining_tickets', models.IntegerField(blank=True, null=True)),
                ('airline_Companie_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.airline_companie')),
                ('destination_countrie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination_countrie_id', to='base.countrie')),
                ('origin_countrie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='origin_countrie_id', to='base.countrie')),
            ],
        ),
        migrations.CreateModel(
            name='User_Role',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('name_role', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='adminstrator',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.customer', unique=True)),
                ('flight_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.flight', unique=True)),
            ],
        ),
    ]
