# Generated by Django 2.2.2 on 2019-06-26 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0003_auto_20190624_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='password',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]