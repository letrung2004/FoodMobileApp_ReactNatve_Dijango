# Generated by Django 5.1.2 on 2024-12-13 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_rename_avatar_restaurant_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='upload/%Y/%m'),
        ),
    ]
