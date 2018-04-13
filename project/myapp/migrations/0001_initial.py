# Generated by Django 2.0.2 on 2018-04-12 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=164)),
                ('last_name', models.CharField(max_length=164)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
