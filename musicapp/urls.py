
from django.urls import path
from . import views

app_name = 'musicapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addRecord/', views.addRecord, name='addRecord'),
    path('<int:id>/details/', views.details, name='details'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/update/updateRecord', views.updateRecord, name='updateRecord'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/lyrics/', views.lyrics, name='lyrics'),
]


