# Generated by Django 2.0.8 on 2018-08-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180828_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Mail'), ('not-specified', 'Not Specified')], max_length=80, null=True),
        ),
    ]
