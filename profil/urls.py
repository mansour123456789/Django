from django.urls import path 
from . import views



urlpatterns = [
  
    # path('', views.proflie,name='index'),
  #  path('', views.importExcel,name='file'),
    # path('condition/', views.conditionn,name='conditin'),
    # path('choix/', views.choix,name='choix'),
    # path('update/', views.update,name='update'),
    path('table<int:id>', views.table,name='table'),
     path('filee', views.aa,name='filee'),
    path('file', views.file,name='file'),
    
    path('condition', views.condition,name='condition'),
    path('rute', views.rutee,name='rute'),
    path('upload', views.upload,name='upload'),
    
    
    
]
