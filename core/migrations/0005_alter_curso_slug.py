# Generated by Django 4.2 on 2023-04-29 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_curso_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
