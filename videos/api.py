from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import VideoSerializer
from .models import Video


class VideoListAPI(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer