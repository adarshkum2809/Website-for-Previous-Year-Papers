# Generated by Django 5.0.2 on 2024-05-26 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='caption',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='uploadimage',
            name='image',
            field=models.FileField(upload_to='images'),
        ),
    ]