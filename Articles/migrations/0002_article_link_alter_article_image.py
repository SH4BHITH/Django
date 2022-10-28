# Generated by Django 4.0 on 2022-10-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Link',
            field=models.CharField(default='https://h4ckr0pz.ml', max_length=2500),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.CharField(max_length=3000),
        ),
    ]
