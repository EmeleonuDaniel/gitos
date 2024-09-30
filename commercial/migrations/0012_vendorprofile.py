# Generated by Django 5.1.1 on 2024-09-29 15:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0011_rename_userprofile_sellerprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=255)),
                ('WA_link', models.URLField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('seller_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='commercial.sellerprofile')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
