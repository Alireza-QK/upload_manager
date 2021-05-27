from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import UploadManager
from .forms import UploadManagerForm


class ImageListView(ListView):
    model = UploadManager
    template_name = 'manager/image_list.html'


class CreateUploadView(CreateView):
    model = UploadManager
    form_class = UploadManagerForm
    template_name = 'manager/upload.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = { 'form': form }
        return render(request, self.template_name, context)
    