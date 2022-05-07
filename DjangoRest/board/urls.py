from django.conf.urls import include
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('viewjson/', views.viewjson, name="viewjson"),
    path('boardlist/', views.boardList, name="boardlist"),
    path('boardView/<str:pk>/', views.boardView, name="boardView"),
    path('boardInsert/', views.boardInsert, name="boardInsert"),
    path('boardupdata/<str:pk>/', views.boardupdata, name="boardupdata"),
    path('boardDelete/<str:pk>/', views.boardDelete, name="boardDelete"),
]
