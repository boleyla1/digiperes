# Generated by Django 5.1 on 2024-09-02 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_brand_category_product_brand_brand_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
