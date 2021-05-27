import uuid
import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from .utils import upload_image_path

class UploadManager(models.Model):
	"""
		Represents a uploader image file
	"""

	title = models.CharField(verbose_name='title image', max_length=128, blank=True)

	image = models.ImageField(verbose_name='image', upload_to=upload_image_path)
	thumbnail = ImageSpecField(
		source='image',
		processors=[ResizeToFill(530, 470)],
		options={'quality': 1000},
	)

	image_width = models.CharField(verbose_name='image width', max_length=16, default='0', blank=True)
	image_height = models.CharField(verbose_name='image height', max_length=16, default='0', blank=True)
	type_image = models.CharField(verbose_name='type image', max_length=12, default='jpg', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
