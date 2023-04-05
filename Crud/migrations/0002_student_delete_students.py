# Generated by Django 4.2 on 2023-04-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
