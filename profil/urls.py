from django.urls import path 
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/index.html'),name='index'),
    path('indexx', TemplateView.as_view(template_name='profil/setting.html'),name='indexx'),
  #  path('', views.importExcel,name='file'),
    # path('condition/', views.conditionn,name='conditin'),
     path('KKK/',  TemplateView.as_view(template_name='dashboard/KKK.html'),name='KKK'),
    # path('update/', views.update,name='update'),
    path('table<int:id>', views.table,name='table'),
    path('filter<int:id>', views.filter,name='filter'),
    path('getfilter<int:id>', views.getfilter,name='getfilter'),
     path('filee', views.aa,name='filee'),
    path('file', views.file,name='file'),
     path('condition', views.Condition,name='Condition'),
    path('condition<int:id>', views.conditionn,name='condition'),
    
     path('resultat', views.res,name='resulta'),
    path('resultat<int:id>', views.ress,name='resultat'),
    path('rute', views.rutee,name='rute'),
    path('upload', views.upload,name='upload'),
    
    path('export<int:id>', views.export,name='export'),
    path('test<int:id>', views.test,name='test'),
    path('delit<int:id>', views.delit,name='delit'),
     path('ptest', views.ptest,name='ptest'),
      path('page_test', views.page_test,name='page_test'),
      path('hestorique<int:id>', views.hestorique,name='hestorique'),
    
    
    
]
