# Generated by Django 2.2.7 on 2020-06-01 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
