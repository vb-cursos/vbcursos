# Generated by Django 4.2 on 2023-05-02 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_curso_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqGeral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=150, verbose_name='Pegunta Faq')),
                ('resposta', models.TextField(verbose_name='Resposta Faq')),
            ],
        ),
    ]
