# Generated by Django 4.2.4 on 2023-11-29 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
