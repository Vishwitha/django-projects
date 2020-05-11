# Generated by Django 3.0.3 on 2020-05-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256)),
                ('lastname', models.CharField(max_length=256)),
                ('phone', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('length', models.PositiveIntegerField()),
                ('release_year', models.PositiveIntegerField()),
            ],
        ),
    ]
