# Generated by Django 2.2.7 on 2020-11-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_limu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='position',
            field=models.CharField(max_length=50),
        ),
    ]
