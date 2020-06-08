# Generated by Django 2.1 on 2020-06-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('about_church', models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'ChurchDetails',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'contacts',
            },
        ),
    ]