from django.urls import path
from .views import WhiteboardList, WhiteboardDetail

urlpatterns = [
    path('', WhiteboardList.as_view(), name='whiteboard_list'),
    path('<int:pk>', WhiteboardDetail.as_view(), name='whiteboard_detail'),
]