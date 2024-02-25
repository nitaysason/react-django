
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('drugs/', views.drugs),
    path('adddrug', views.adddrug),
    path('deldrug/<int:id>', views.deldrug),
    path('updatedrug/<int:id>', views.updatedrug),
 
]

