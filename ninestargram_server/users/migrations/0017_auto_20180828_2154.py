# Generated by Django 2.0.8 on 2018-08-28 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20180828_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Mail'), ('female', 'Female'), ('not-specified', 'Not Specified')], max_length=80, null=True),
        ),
    ]