from django.db import models

# Create your models here.
from django.conf import settings	#photo model

def user_path(instance, filename):	#instance 는 photo 객체, filename = filename
	from random import choice	#string으로 나온 결과에서 하나의 문자열만 뽑기
	import string
	arr = [choice(string.ascii_letters)for _ in range(8)]	#무작위8자
	pid = ''.join(arr)	#파일아이디 생성
	extension = filename.split('.')[-1]	#파일이름에서 확장자 가져오기
	return '%s/%s.%s' %(instance.owner.username, pid, extension)

class Photo(models.Model):
	image = models.ImageField(upload_to = user_path)	#업로드 위치 정함
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,)	#1:N관계
	thumbnail_image = models.ImageField(blank=True)	#form입력 (선택)
	comment = models.CharField(max_length = 255)
	pub_date = models.DateTimeField(auto_now_add=True)	#자동 생성

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,)	#현계정의 사용자
	nickname = models.CharField(max_length = 64)
	profile_photo = models.ImageField(blank=True)