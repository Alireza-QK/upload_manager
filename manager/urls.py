from django.urls import path
from manager.views import ImageListView, CreateUploadView

app_name = 'manager'

urlpatterns = [
    path('', ImageListView.as_view(), name="list_image"),
    path('upload/', CreateUploadView.as_view(), name="upload"),
    path('delete/<int:pk>', DeleteUploadView.as_view(), name="delete"),
]
