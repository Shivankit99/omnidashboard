# Generated by Django 2.2.28 on 2022-06-03 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnidash', '0002_auto_20220603_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='desi',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
