from django.urls import path
from .views import PhotoList, PhotoDelete, PhotoDetail, PhotoUpdate, PhotoCreate
from django.conf.urls.static import static
from django.conf import settings


app_name = "photo"
#app_name 설정을 통해 namespace확보
#prevents url pattern이름 겹치는 것 with other apps

urlpatterns = [
	path("create/", PhotoCreate.as_view(), name = 'create'),
	path("delete/<int:pk>/", PhotoDelete.as_view(), name = 'delete'),
	path("update/<int:pk>/", PhotoUpdate.as_view(), name = 'update'),
	path("detail/<int:pk>/", PhotoDetail.as_view(), name = 'detail'),
	path("", PhotoList.as_view(), name = 'index'),
	#<int:pk> : 해당 작성에 대한 번호로 이동해야 상세 페이지 및 그 글 삭제/수정 가능..
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)