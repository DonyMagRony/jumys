# Generated by Django 5.1.4 on 2024-12-06 12:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('follows', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connection_requests_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='connection',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connection_requests_sent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='followee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='referenceletter',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reference_letters_written', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='referenceletter',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reference_letters_received', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together={('sender', 'receiver')},
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'followee')},
        ),
    ]
