# Generated by Django 3.2.5 on 2021-07-07 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='portofolio/projects/static/img/")'),
        ),
    ]
