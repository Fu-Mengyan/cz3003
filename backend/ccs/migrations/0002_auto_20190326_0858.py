# Generated by Django 2.1.7 on 2019-03-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='key_indicator_PSI',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='report_person_region',
            field=models.CharField(choices=[('southWest', 'South West'), ('northWest', 'NorthWest'), ('central', 'Central'), ('northEast', 'North East'), ('southEast', 'South East')], default='southWest', max_length=20),
        ),
    ]