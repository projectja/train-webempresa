# Generated by Django 3.1.7 on 2021-10-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='service',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
