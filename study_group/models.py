from django.db import models
import study_group

from user.models import User

# Create your models here.

class Study(models.Model):
    class Meta:
        db_table = 'study_post'
        
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    create_dt = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    thumbnail_img = models.ImageField(upload_to='media', height_field=None, default='default.jpeg', blank=True)
    on_off_line = models.BooleanField(default = None, null=True) # None 0 1 로 구분이 안된다면 CharField로 구분
    headcount = models.IntegerField(default = None, null=True) #IntegerChoices? 선택인원 최소 2~10 지정할 수 있으면 지정하기
    # category = #TODO 경민 - 조사 후 카테고리, 나눈 뒤 모델 생성
    
class Student(models.Model):
    class Meta:
        db_table = 'student'
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Study, on_delete=models.CASCADE)
    join_dt = models.DateField(auto_now_add = True)
    is_accept = models.BooleanField(default=None, null=True)