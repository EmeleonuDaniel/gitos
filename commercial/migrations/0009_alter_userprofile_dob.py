# Generated by Django 5.1 on 2024-09-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0008_alter_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
    ]
