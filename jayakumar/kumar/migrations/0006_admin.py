# Generated by Django 4.0.4 on 2022-05-24 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumar', '0005_alter_flipkart_age_alter_morning_dosa_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=50, null=True)),
                ('adminpassword', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'admin',
                'verbose_name_plural': 'admins',
            },
        ),
    ]
