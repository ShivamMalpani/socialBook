# Generated by Django 4.1 on 2022-09-02 08:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_profile_followers_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c3892768-8b90-4bcd-9e6d-25dd9af0f665'), primary_key=True, serialize=False),
        ),
    ]
