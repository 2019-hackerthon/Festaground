# Generated by Django 2.2.3 on 2019-08-04 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_festa', '0003_auto_20190803_1315'),
        ('app_festaNow', '0008_now_post_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lost_Found',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200)),
                ('post_type', models.CharField(choices=[('분실', '분실'), ('습득', '습득')], max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('festa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_festa.Festa')),
            ],
        ),
    ]
