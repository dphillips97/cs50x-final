# Generated by Django 4.2.6 on 2023-10-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogtracks', '0013_alter_animal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
    ]