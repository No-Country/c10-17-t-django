# Generated by Django 4.1.4 on 2023-04-20 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour_guide', '0003_report'),
        ('tourist_spot', '0002_favorite_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guide_site',
            name='dni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour_guide.guide'),
        ),
    ]
