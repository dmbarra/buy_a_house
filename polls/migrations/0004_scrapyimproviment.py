# Generated by Django 3.1.6 on 2021-02-19 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_basiccrawler_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapyImproviment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.CharField(max_length=1000)),
                ('improved', models.CharField(max_length=1000)),
            ],
        ),
    ]
