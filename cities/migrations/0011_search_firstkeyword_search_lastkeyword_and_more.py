# Generated by Django 4.0.1 on 2022-05-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0010_rename_operations_new_operations'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='firstkeyword',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='lastkeyword',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='search',
            name='secondkeyword',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
