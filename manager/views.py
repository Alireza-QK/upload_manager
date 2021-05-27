from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from PIL import Image
from .models import UploadManager
from .forms import UploadManagerForm


class ImageListView(ListView):
    model = UploadManager
    template_name = 'manager/image_list.html'
    paginate_by = 5


class CreateUploadView(CreateView):
    # model = UploadManager
    form_class = UploadManagerForm
    template_name = 'manager/upload.html'
    success_url = reverse_lazy('manager:list_image')

    def form_valid(self, form):
        response = form.save(commit=False)
        
        context = {
            'form': form
        }

        if form.is_valid():
            image = form.cleaned_data.get('image')
            title = form.cleaned_data.get('title')
            if title is None or title == '':
                title = image.name
            
            infoImage = Image.open(image)
            width, height = infoImage.size

            uplader = UploadManager.objects.create(
                title=title,
                image=image,
                image_width=width,
                image_height=height,
                type_image=infoImage.format
            )
            if uplader:
                return redirect('manager:upload')
        
        return render(self.request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        form = self.form_class
        context = { 'form': form }
        return render(request, self.template_name, context)
