from django.urls import path 
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/index.html'),name='index'),
    # path('', views.proflie,name='index'),
  #  path('', views.importExcel,name='file'),
    # path('condition/', views.conditionn,name='conditin'),
    # path('choix/', views.choix,name='choix'),
    # path('update/', views.update,name='update'),
    path('table<int:id>', views.table,name='table'),
     path('filee', views.aa,name='filee'),
    path('file', views.file,name='file'),
     path('condition', views.Condition,name='Condition'),
    path('condition<int:id>', views.conditionn,name='condition'),
    
     path('resultat', views.res,name='resulta'),
    path('resultat<int:id>', views.ress,name='resultat'),
    path('rute', views.rutee,name='rute'),
    path('upload', views.upload,name='upload'),
    
    
    
]
