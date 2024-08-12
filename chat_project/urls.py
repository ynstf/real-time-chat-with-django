from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from chat import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('join/<int:id>', views.join, name='join'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('chat/', include('chat.urls')),
]
