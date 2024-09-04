# Generated by Django 5.1 on 2024-08-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_color_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, related_name='محصولات', to='product.color', verbose_name='رنگ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.SmallIntegerField(default=0, verbose_name='تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, related_name='محصولات', to='product.size', verbose_name='سایز'),
        ),
    ]
