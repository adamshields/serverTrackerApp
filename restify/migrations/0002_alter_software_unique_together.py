# Generated by Django 3.2.6 on 2021-09-27 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restify', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='software',
            unique_together={('software_name', 'software_version')},
        ),
    ]
