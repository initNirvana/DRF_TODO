from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=50) # 제목
    author = models.CharField(max_length=50) # 작성자
    image = models.CharField(max_length=200) # 이미지
    description = models.TextField() # 설명
    price = models.IntegerField() # 가격

