# Generated by Django 2.2.28 on 2022-06-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reportingmanager', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('Mail', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
            ],
        ),
    ]
