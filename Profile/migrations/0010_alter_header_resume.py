# Generated by Django 3.2.4 on 2021-06-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0009_delete_projects12'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='resume',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
