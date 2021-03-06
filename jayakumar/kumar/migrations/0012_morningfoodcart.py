# Generated by Django 4.0.4 on 2022-05-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumar', '0011_morningfood_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='morningfoodcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.IntegerField(max_length=50, null=True)),
                ('count', models.IntegerField(max_length=50, null=True)),
                ('img', models.CharField(max_length=500, null=True)),
            ],
            options={
                'verbose_name': 'morningitems',
                'verbose_name_plural': 'morningitemss',
            },
        ),
    ]
