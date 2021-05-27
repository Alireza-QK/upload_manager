from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import UploadManager
from .forms import UploadManagerForm


class ImageListView(ListView):
    model = UploadManager
    template_name = 'manager/image_list.html'
    