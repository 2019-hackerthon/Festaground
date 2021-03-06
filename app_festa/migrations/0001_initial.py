# Generated by Django 2.1.8 on 2019-08-07 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Festa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('schedule_start', models.DateField(verbose_name='date published')),
                ('schedule_end', models.DateField(verbose_name='date published')),
                ('space', models.CharField(max_length=200)),
                ('purchase_link', models.CharField(max_length=200)),
                ('host', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('detail_map', models.CharField(max_length=200)),
                ('precautions', models.TextField()),
                ('notice', models.TextField()),
                ('poster', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
            options={
                'ordering': ['schedule_start'],
            },
        ),
        migrations.CreateModel(
            name='RegisterNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_num', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('festa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_festa.Festa')),
            ],
        ),
        migrations.AddField(
            model_name='festa',
            name='number',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_festa.RegisterNum'),
        ),
        migrations.AddField(
            model_name='audience',
            name='festa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_festa.Festa'),
        ),
    ]
