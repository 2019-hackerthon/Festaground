# Generated by Django 2.2.3 on 2019-07-19 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_festa', '0003_auto_20190719_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='festa',
            old_name='title',
            new_name='name',
        ),
    ]