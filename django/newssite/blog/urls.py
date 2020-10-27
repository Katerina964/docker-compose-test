from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import homePageView
from . import views

app_name = 'blog'

urlpatterns = [
    path('',views.homePageView, name='homePageView'),
    path('blog/<int:pk>/', views.detail, name='detail'),
    path('python_developer', views.python_developer, name='python_developer'),
    path('java_developer', views.java_developer, name='java_developer'),
    path('create_resume', views.create_resume, name='create_resume'),
    path('create_vacancy', views.create_vacancy, name='create_vacancy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
