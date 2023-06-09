# Generated by Django 3.2.18 on 2023-03-19 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Фирма')),
                ('content', models.TextField(blank=True, null=True, verbose_name='характеристики')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='цена')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='telefon.brand')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
                'db_table': 'Phone',
                'ordering': ('price',),
            },
        ),
    ]
