from django import forms
from django.core.exceptions import ValidationError
from upload_validator import FileTypeValidator

from .models import UploadManager


class UploadManagerForm(forms.ModelForm):

	image = forms.FileField(
		label='', help_text="Formats accepted: JPEG nd PNG nd JPG nd GIF",
		validators=[FileTypeValidator(
			allowed_types=[ 'image/jpeg','image/jpg', 'image/png', 'image/gif']
		)]
	)

	class Meta:
		model = UploadManager
		fields = ('image', 'title')
	
	def clean_image(self):
		image = self.cleaned_data.get('image')
		fileSize = image.size
		megabyte_limit = 3.0

		if filesize > megabyte_limit * 1024 * 1024:
			raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

		return image
