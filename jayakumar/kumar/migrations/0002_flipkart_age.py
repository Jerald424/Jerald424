# Generated by Django 4.0.4 on 2022-05-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flipkart',
            name='age',
            field=models.CharField(max_length=50, null=True),
        ),
    ]