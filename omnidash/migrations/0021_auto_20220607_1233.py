# Generated by Django 2.2.28 on 2022-06-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omnidash', '0020_auto_20220607_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='dfrom',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leave',
            name='dto',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rem',
            name='dfrom',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rem',
            name='dto',
            field=models.DateField(),
        ),
    ]
