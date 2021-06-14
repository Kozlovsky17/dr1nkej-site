from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from drink import settings

urlpatterns = [
    #path('', views.post_list, name= 'post_list'),
    path('', views.index, name= 'index'),
    path('post/new/', views.post_new, name='post_new'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout, name = 'logout'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('profile/', views.profile, name='profile'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)