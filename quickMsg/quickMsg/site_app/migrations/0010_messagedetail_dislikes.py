# Generated by Django 4.2.3 on 2023-09-21 10:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0009_messagedetail_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagedetail',
            name='dislikes',
            field=models.ManyToManyField(related_name='message_post_dislike', to=settings.AUTH_USER_MODEL, verbose_name='Dislikes'),
        ),
    ]
