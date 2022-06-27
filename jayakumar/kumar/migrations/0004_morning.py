# Generated by Django 4.0.4 on 2022-05-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kumar', '0003_alter_flipkart_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='morning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tea', models.CharField(max_length=50, null=True)),
                ('idly', models.CharField(max_length=50, null=True)),
                ('dosa', models.CharField(max_length=50, null=True)),
                ('pongal', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'morning',
                'verbose_name_plural': 'mornings',
            },
        ),
    ]
