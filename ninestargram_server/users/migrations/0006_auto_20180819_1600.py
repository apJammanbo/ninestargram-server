# Generated by Django 2.0.8 on 2018-08-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180819_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Mail'), ('not-specified', 'Not Specified')], max_length=80, null=True),
        ),
    ]
