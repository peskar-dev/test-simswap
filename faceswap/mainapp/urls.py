from django.urls import path
from django.views.generic import TemplateView

from .views import download_photo, home, process_photo

urlpatterns = [
    path("", home, name="home"),
    path("process_photo/", process_photo, name="process_photo"),
    path(
        "uploading_photos/",
        TemplateView.as_view(template_name="uploading_photos.html"),
        name="uploading-photos",
    ),
    path("process_photo/", process_photo, name="process_photo"),
    path(
        "download_photo/<str:dirkey>/", download_photo, name="download_photo"
    ),
    path(
        "result/<slug:dirkey>",
        TemplateView.as_view(template_name="photo_ready.html"),
        name="result",
    ),
    path(
        "competition/",
        TemplateView.as_view(template_name="competition.html"),
        name="competition",
    ),
    path("process/", process_photo, name="process"),
]
