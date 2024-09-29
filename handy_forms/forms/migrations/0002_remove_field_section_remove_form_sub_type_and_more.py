# Generated by Django 5.1 on 2024-09-22 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='field',
            name='section',
        ),
        migrations.RemoveField(
            model_name='form',
            name='sub_type',
        ),
        migrations.RemoveField(
            model_name='form',
            name='type',
        ),
        migrations.RemoveField(
            model_name='formattribute',
            name='autocomplete',
        ),
        migrations.AlterField(
            model_name='form',
            name='form_name',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
