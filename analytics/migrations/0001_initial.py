# Generated by Django 5.2 on 2025-04-10 12:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales_data', '0001_initial'),
        ('spotify_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductClusterProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.cluster')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales_data.product')),
            ],
        ),
        migrations.CreateModel(
            name='TrackClusterAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics.cluster')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spotify_data.track')),
            ],
        ),
    ]
