
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view() , name= 'homepage'),
    path('edit_album/<int:pk>/', views.EditAlbumView.as_view() , name= 'edit_album'),
    path('edit_name/<int:pk>/', views.EditNameView.as_view() , name= 'edit_name'),
    path('delete_post/<int:pk>/', views.DeletePostView.as_view() , name= 'delete_post'),
    path('database/', views.DatabaseView.as_view(), name= 'database'),
    path('musician_app/', include( 'musician_app.urls' )),
    path('album_app/', include( 'album_app.urls' )),
    
]
