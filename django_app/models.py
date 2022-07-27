from distutils.command.upload import upload
from django.db import models
from django.utils.safestring import mark_safe

class Post(models.Model):
    pass

class Blog(models.Model):
    #제목 필드
    title = models.CharField(max_length=100)
    #내용 필드
    content = models.TextField()
    #생성시간 필드
    created_at = models.DateTimeField(auto_now_add=True)
    #수정시간 필드
    updated_at = models.DateTimeField(auto_now=True)
    #공개여부 필드
    is_public = models.BooleanField(default=False,verbose_name="공개여부")
    #이미지 업로드 필드 db는 이미지의 경로에 대한 텍스트만 저장되고 실제 이미지는 스토리지에 저장된다.

    #upload_to는 root경로인 media 폴더 하위에 이미지가 쌓일 경로를 지정할 수 있다.
    #이미지가 많을수록 각 폴더별로 관리를 해야 이미지를 가져올때 속도가 빠르기 때문
    photo = models.ImageField(blank=True,upload_to='django_images/windows/%Y/%m/%d')


    def __str__(self):
        return self.content

    def content_length(self):
        return len(self.content)
    content_length.short_description = "내용 글자수"

    def photo_tag(self):
        if self.photo:
            #mark_safe 처리해줘야지 이미지가 태그형식이 아닌 이미지그대로 나옴
            return mark_safe(f'<img src="{self.photo.url}" style="width: 100px;" />')
        return None