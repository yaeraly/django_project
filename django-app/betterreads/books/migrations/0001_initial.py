# Generated by Django 3.0.5 on 2020-05-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('blurb', models.TextField(blank=True)),
                ('num_pages', models.IntegerField(blank=True)),
                ('price', models.FloatField(blank=True)),
                ('in_print', models.BooleanField(default=True)),
            ],
        ),
    ]
