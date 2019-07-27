# Generated by Django 2.2.3 on 2019-07-27 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Now',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('password', models.CharField(max_length=20)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title2', models.CharField(max_length=200)),
                ('writer2', models.CharField(max_length=100)),
                ('pub_date2', models.DateTimeField(verbose_name='date published')),
                ('password2', models.CharField(max_length=20)),
                ('body2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Commentt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_team', models.CharField(max_length=200)),
                ('content_team', models.TextField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_festaNow.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Commentn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_now', models.CharField(max_length=200)),
                ('content_now', models.TextField()),
                ('now', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_festaNow.Now')),
            ],
        ),
        migrations.CreateModel(
            name='Commenth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer_home', models.CharField(max_length=200)),
                ('content_home', models.TextField()),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_festaNow.Home')),
            ],
        ),
    ]
