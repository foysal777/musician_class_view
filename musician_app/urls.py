
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musician/', views.MusicianCreateView.as_view() , name='musician' ),
]