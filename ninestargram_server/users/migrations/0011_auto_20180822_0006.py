# Generated by Django 2.0.8 on 2018-08-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180821_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('not-specified', 'Not Specified'), ('female', 'Female'), ('male', 'Mail')], max_length=80, null=True),
        ),
    ]
