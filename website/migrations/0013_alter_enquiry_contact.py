# Generated by Django 4.2.7 on 2023-12-09 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_enquiry_comment_enquiry_status_alter_enquiry_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='contact',
            field=models.IntegerField(max_length=11),
        ),
    ]
