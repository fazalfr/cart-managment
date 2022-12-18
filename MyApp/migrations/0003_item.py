# Generated by Django 4.1.2 on 2022-12-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_users_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
    ]
