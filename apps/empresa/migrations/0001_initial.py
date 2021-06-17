# Generated by Django 3.2.4 on 2021-06-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome da empresa', max_length=100)),
                ('cnpj', models.CharField(help_text='CNPJ da empresa', max_length=14)),
            ],
        ),
    ]