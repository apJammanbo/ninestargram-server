# Generated by Django 2.0.8 on 2018-08-19 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reator',
            new_name='creator',
        ),
    ]
