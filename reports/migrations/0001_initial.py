# Generated by Django 4.2.7 on 2024-11-18 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('vehicle_involved', models.CharField(max_length=252)),
                ('other_vehicle_involved', models.CharField(blank=True, max_length=252, null=True)),
                ('incident_type', models.CharField(max_length=252)),
                ('cause', models.TextField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_updated_time', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='users/%Y/%m')),
            ],
        ),
    ]
