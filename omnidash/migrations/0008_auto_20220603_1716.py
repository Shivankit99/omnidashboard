# Generated by Django 2.2.28 on 2022-06-03 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omnidash', '0007_auto_20220603_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='username',
        ),
        migrations.RemoveField(
            model_name='rem',
            name='username',
        ),
    ]
