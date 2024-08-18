# TaskMan/urls.py

from django.contrib import admin

from django.urls import path, include
from tasks import views as task_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('tasks.urls')),
    path('', task_views.activity_feed, name='index'),

    
]
