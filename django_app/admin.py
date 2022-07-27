from django.contrib import admin

from .models import Blog
# Register your models here.
#admin.site.register(Blog)
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    #list_* , search_* 는 임의의 변수명이 아니라 장고 admin의 객체
    list_display = ['id','title','content','photo_tag','created_at','updated_at','content_length','is_public']
    list_filter = ['created_at','is_public']
    search_fields = ['title','content']
