# Generated by Django 3.1.7 on 2021-04-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloging', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='contents',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
