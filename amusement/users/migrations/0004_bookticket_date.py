# Generated by Django 3.2.7 on 2024-03-02 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240301_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookticket',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
