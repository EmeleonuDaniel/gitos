# Generated by Django 5.1 on 2024-09-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('image', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
