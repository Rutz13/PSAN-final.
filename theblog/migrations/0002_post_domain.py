# Generated by Django 4.0.4 on 2022-06-11 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='domain',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
