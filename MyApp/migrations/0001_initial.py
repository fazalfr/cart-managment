# Generated by Django 4.1.2 on 2022-11-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
