from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('signup', views.signupPage, name='signupPage'),
    path('login', views.loginPage, name='loginPage'),
    path('logout', views.logoutPage, name='logoutPage'),
    path('addResume',views.addResume,name='addResume'),
    path('viewResume',views.viewResume,name='viewResume'),
    path('listResume',views.listResume,name='viewResume'),
    
    
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
