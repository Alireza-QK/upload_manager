import uuid
import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from .utils import *

class UploadManager(models.Model):
    """
		Represents a uploader image file
	"""

    pass
