# Generated by Django 4.0.4 on 2022-05-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumar', '0010_morningfood'),
    ]

    operations = [
        migrations.AddField(
            model_name='morningfood',
            name='img',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
