# Generated by Django 5.1 on 2024-08-23 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics', verbose_name='عکس پروفایل کاربر'),
        ),
    ]
