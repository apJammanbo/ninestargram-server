# Generated by Django 2.0.8 on 2018-08-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180819_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('not-specified', 'Not Specified'), ('male', 'Mail')], max_length=80, null=True),
        ),
    ]
