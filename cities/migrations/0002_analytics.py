# Generated by Django 4.0.1 on 2022-05-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200)),
                ('meaning', models.TextField()),
                ('href', models.URLField(max_length=1000)),
                ('firstkeyword', models.CharField(max_length=200, null=True)),
                ('secondkeyword', models.CharField(max_length=200, null=True)),
                ('lastkeyword', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
