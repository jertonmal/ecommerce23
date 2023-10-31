# Generated by Django 4.2.5 on 2023-10-23 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_tipo_variacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
