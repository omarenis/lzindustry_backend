# Generated by Django 4.2.1 on 2023-05-06 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('governorate', models.TextField()),
                ('region', models.TextField()),
                ('delegation', models.TextField()),
                ('zip_code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('number_products', models.FloatField(default=0)),
                ('number_tags', models.FloatField(default=0)),
                ('address', models.TextField()),
                ('localisation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store_management.localisation')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth_module.profile')),
            ],
        ),
    ]
