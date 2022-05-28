from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from members import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Home,name='Home'),
    path('register', views.register, name='register'),
    path('pay',views.pay1,name='pay1'),
    path('paydone',views.paydone,name='paydone'),
    path('regdone',views.regdone,name='regdone'),  
    path('HowitWorks',views.HowitWorks,name='HowitWorks'),
    path('insert/',views.insert),
    path('facelogin/',views.facelogin,name="nakamu"),
    path('external/',views.external),
]  
if settings.DEBUG:
        urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

