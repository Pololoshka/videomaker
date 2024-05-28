from django.urls import path

from videomaker.views import VideoAPIView

urlpatterns = [
    path("createvideo/", VideoAPIView.as_view()),
]
