# Generated by Django 3.2.3 on 2021-05-27 08:15

from django.db import migrations, models
import manager.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, verbose_name='title image')),
                ('image', models.ImageField(upload_to=manager.utils.upload_image_path, verbose_name='image')),
                ('image_width', models.CharField(blank=True, default='0', max_length=16, verbose_name='image width')),
                ('image_height', models.CharField(blank=True, default='0', max_length=16, verbose_name='image height')),
                ('type_image', models.CharField(blank=True, default='jpg', max_length=12, verbose_name='type image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
