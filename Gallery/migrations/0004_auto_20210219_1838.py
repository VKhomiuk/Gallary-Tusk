# Generated by Django 3.1.6 on 2021-02-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0003_auto_20210218_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Photo'),
        ),
    ]