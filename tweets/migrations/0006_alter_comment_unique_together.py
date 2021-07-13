# Generated by Django 3.2.4 on 2021-06-30 12:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0005_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('user', 'tweet')},
        ),
    ]