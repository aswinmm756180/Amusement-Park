# Generated by Django 3.2.7 on 2024-03-04 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_app', '0003_auto_20240302_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='password2',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
