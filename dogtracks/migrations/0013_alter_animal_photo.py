# Generated by Django 4.2.6 on 2023-10-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogtracks', '0012_alter_visit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]