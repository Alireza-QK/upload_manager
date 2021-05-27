import uuid
import os


def upload_image_path(instance, filename):
	"""
		this function generate unique file name
	"""
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('manager/images', filename)
