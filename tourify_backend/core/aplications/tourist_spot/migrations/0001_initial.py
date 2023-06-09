# Generated by Django 4.1.3 on 2023-04-20 03:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tour_guide', '0003_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id_site', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
                ('latitude', models.CharField(max_length=10)),
                ('lenght', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('budget', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('validation', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Visit_site',
            fields=[
                ('visit_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date_visitdate_view', models.DateTimeField(auto_now=True)),
                ('qualification', models.CharField(choices=[('M', 'Malo'), ('R', 'Regular'), ('B', 'Bueno'), ('MB', 'Muy bueno'), ('E', 'Excelente')], max_length=10)),
                ('trasport', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('housing', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('meal', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('coment', models.CharField(blank=True, max_length=300, null=True)),
                ('recomentadion', models.CharField(blank=True, max_length=100, null=True)),
                ('id_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_spot.site')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo_visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('visit_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_spot.visit_site')),
            ],
        ),
        migrations.CreateModel(
            name='Photo_site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField(auto_now=True)),
                ('link', models.CharField(max_length=100)),
                ('id_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_spot.site')),
            ],
        ),
        migrations.CreateModel(
            name='Guide_site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_register', models.DateTimeField(auto_now=True)),
                ('date_update_site', models.DateTimeField(blank=True, null=True)),
                ('description_update', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo'), ('S', 'Suspendido')], max_length=30)),
                ('dni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_guide.guide')),
                ('id_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_spot.site')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite_site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('id_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_spot.site')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('nro_view', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True)),
                ('date_view', models.DateTimeField(auto_now=True)),
                ('id_site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tourist_spot.site')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
