# Generated by Django 2.0 on 2018-11-01 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_readed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='readed',
            new_name='readed_num',
        ),
    ]
