# Generated by Django 2.1 on 2020-06-03 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swapp', '0004_auto_20200603_0808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutchurch',
            options={'verbose_name_plural': 'AboutChurch'},
        ),
        migrations.AddField(
            model_name='aboutchurch',
            name='church_branches',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
