# Generated by Django 4.2.7 on 2023-11-29 16:30

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField(max_length=10)),
            ],
            options={
                'db_table': 'Enquiry',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
