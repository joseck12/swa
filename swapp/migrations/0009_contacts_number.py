# Generated by Django 2.1 on 2020-06-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swapp', '0008_aboutchurch_website_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='number',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
    ]
