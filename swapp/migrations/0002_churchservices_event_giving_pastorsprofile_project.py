# Generated by Django 2.1 on 2020-06-02 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChurchServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(blank=True, max_length=225, null=True)),
                ('service_details', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'verbose_name_plural': 'ChurchServices',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(blank=True, max_length=225, null=True)),
                ('event_description', models.TextField(blank=True, max_length=500, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.CreateModel(
            name='Giving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_images', models.ImageField(default='', upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'givings',
            },
        ),
        migrations.CreateModel(
            name='PastorsProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, default='', upload_to='images')),
            ],
            options={
                'verbose_name_plural': 'PastorsProfile',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(blank=True, max_length=225, null=True)),
                ('project_link', models.CharField(blank=True, max_length=225, null=True)),
                ('project_description', models.CharField(blank=True, max_length=225, null=True)),
                ('project_image', models.ImageField(blank=True, default='', upload_to='images')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'projects',
            },
        ),
    ]
