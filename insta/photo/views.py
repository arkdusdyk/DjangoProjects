from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail timport DetailView
from .models import Photo
# Create your views here.

#class형 뷰의 generic view를 이용해서 구현
#ListView/CreateView/UpdateView/DeleteView/DetailView 구현

class PhotoList(ListView):
	model = Photo
	template_name_suffix = '_list'
	#PhotoList : 가장 메인에서 보여줄 Logic/model을 불러와서 데이터를 활용하것이라고 기제

class PhotoCreate(CreateView):
	model = Photo
	fields = ['text', 'image']
	template_name_suffix = '_create'
	success_url ='/'
	#PhotoCreate : 모델 생성할때 채워야할 필드확인, 연결된 템플릿 이름은 Photo_to_create
	#if success -> back to main page
class PhotoUpdate(UpdateView):
	model = Photo
	fields = ['text','image']
	template_name_suffix = '_update'
	success_url = '/'
	#photo update : similar to create

class PhotoDelete(DeleteView):
	model = Photo
	template_name_suffix = '_delete'
	success_url = '/'

class PhotoDetail(DetailView):
	model = Photo
	template_name_suffix = '_detail'