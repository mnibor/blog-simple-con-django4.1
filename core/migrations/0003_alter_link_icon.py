# Generated by Django 4.1.2 on 2022-10-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_about_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Icono'),
        ),
    ]
