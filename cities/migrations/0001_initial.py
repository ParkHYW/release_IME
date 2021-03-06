# Generated by Django 4.0.1 on 2022-05-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=1000)),
                ('meaning', models.TextField()),
                ('href', models.URLField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Searchengine',
            },
        ),
    ]
