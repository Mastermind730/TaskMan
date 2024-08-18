from django.contrib import admin

from django.urls import path, include

from tasks import views as task_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', task_views.signup, name='signup'),
    path('login/', task_views.user_login, name='login'),
    path('logout/', task_views.user_logout, name='logout'),
    path('/', task_views.task_list, name='task_list'),
    path('add/', task_views.add_task, name='add_task'),
    path('mark/<int:task_id>/<int:completed>/', task_views.mark_task, name='mark_task'),
    path('delete/<int:task_id>/', task_views.delete_task, name='delete_task'),
    path('activity/', task_views.activity_feed, name='activity_feed'),
]