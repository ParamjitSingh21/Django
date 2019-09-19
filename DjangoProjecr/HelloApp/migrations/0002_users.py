# Generated by Django 2.2.5 on 2019-09-19 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelloApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=264)),
                ('lname', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
