# Generated by Django 4.1.4 on 2022-12-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BlogId', models.CharField(max_length=30)),
                ('Title', models.CharField(max_length=200)),
                ('Author_Name', models.CharField(max_length=300)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
            ],
            options={
                'db_table': 'Blog',
            },
        ),
    ]
