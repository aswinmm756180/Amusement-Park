# Generated by Django 3.2.7 on 2024-03-04 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_bookticket_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookticket',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]