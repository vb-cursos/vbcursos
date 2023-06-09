# Generated by Django 4.2 on 2023-05-05 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_faqgeral'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqgeral',
            options={'verbose_name': 'Faq Geral', 'verbose_name_plural': 'Faq Geral'},
        ),
        migrations.RemoveField(
            model_name='curso',
            name='faq',
        ),
        migrations.AddField(
            model_name='curso',
            name='argumentos',
            field=models.TextField(null=True, verbose_name='Argumentos e dados que comprovam os benefícios do curso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='aulas',
            field=models.IntegerField(null=True, verbose_name='Número de aulas'),
        ),
        migrations.AddField(
            model_name='curso',
            name='autoridade',
            field=models.TextField(null=True, verbose_name='Argumento de autoridade'),
        ),
        migrations.AddField(
            model_name='curso',
            name='cta',
            field=models.CharField(max_length=100, null=True, verbose_name='Chamada para ação do botão (CTA)'),
        ),
        migrations.AddField(
            model_name='curso',
            name='duracao',
            field=models.IntegerField(null=True, verbose_name='Duração do Curso (em horas)'),
        ),
        migrations.AddField(
            model_name='curso',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True, verbose_name='Preço do Curso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='urlVenda',
            field=models.URLField(null=True, verbose_name='Link da página de checkout da Hotmart referente ao curso (pay.hotmart.com)'),
        ),
        migrations.AddField(
            model_name='curso',
            name='urlVideo',
            field=models.URLField(null=True, verbose_name='Link do vídeo da carta de vendas no Youtube'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='beneficios',
            field=models.TextField(null=True, verbose_name='Benefícios de absorver o conteúdo do curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='description',
            field=models.TextField(null=True, verbose_name='Descrição do Curso'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='h1',
            field=models.CharField(max_length=100, null=True, verbose_name='Header Principal (h1) da Página'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='h2',
            field=models.TextField(null=True, verbose_name='Header Secundário (h2) da Página'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título do curso'),
        ),
        migrations.AlterField(
            model_name='faqgeral',
            name='resposta',
            field=models.TextField(null=True, verbose_name='Resposta Faq'),
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='core.curso')),
            ],
            options={
                'verbose_name': 'Módulo',
                'verbose_name_plural': 'Módulos',
            },
        ),
    ]
