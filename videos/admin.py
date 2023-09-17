from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    list_filter = ['title','created_at']
    search_fields = ['title','created_at']
    
    
admin.site.register(Video,VideoAdmin)
admin.site.register(Comment)