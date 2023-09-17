from django.shortcuts import render
from .models import *
from django.views import generic
# Create your views here.


class VideoList(generic.ListView):
    model  = Video
