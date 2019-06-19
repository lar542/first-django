from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30) # 30자 이하의 문자열
    content = models.TextField() # 문자열 길이를 제한하지 않는 긴 문자열

    created_at = models.DateTimeField(auto_now_add=True) # 생성 시각
    updated_at = models.DateTimeField(auto_now=True) # 수정 시각

    # num_stars = models.IntergerField() 숫자필드