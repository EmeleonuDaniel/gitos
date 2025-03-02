# Generated by Django 5.1.1 on 2024-10-07 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0032_remove_product_image_remove_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]
