from django.urls import path
from manager.views import ImageListView

app_name = 'manager'

urlpatterns = [
    path('', ImageListView.as_view(), name="list_image"),
]
