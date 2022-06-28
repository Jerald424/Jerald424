# Generated by Django 4.0.4 on 2022-05-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumar', '0013_coffee_alter_morningfoodcart_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='coffeecart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(max_length=50, null=True)),
                ('count', models.IntegerField(max_length=50, null=True)),
                ('img', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'coffeecart',
                'verbose_name_plural': 'coffeecarts',
            },
        ),
    ]