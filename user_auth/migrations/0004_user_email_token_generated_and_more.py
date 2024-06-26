# Generated by Django 5.0.3 on 2024-04-03 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_user_is_verified_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_token_generated',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email_token_generated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='UserEmailVerificationTrack',
        ),
    ]
