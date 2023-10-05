# Generated by Django 4.2.3 on 2023-09-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0006_siteuser_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteuser',
            name='github',
            field=models.URLField(default='www.github.com', max_length=400, verbose_name='github'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='instagram',
            field=models.URLField(default='www.instagram.com', max_length=400, verbose_name='instagram'),
        ),
        migrations.AddField(
            model_name='siteuser',
            name='twitter',
            field=models.URLField(default='www.twitter.com', max_length=400, verbose_name='twitter:'),
        ),
    ]
