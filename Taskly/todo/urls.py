from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('dashboard', views.dashboard, name="dashboard"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('create-task', views.create_task, name="create-task"),
    path('view-tasks', views.view_tasks, name="view-tasks"),
    path('update-task/<str:pk>', views.update_task, name="update-task"),
    path('delete-task/<str:pk>', views.delete_task, name="delete-task"),
    path('profile-management', views.profile_management, name="profile-management"),
    path('delete-account', views.delete_account, name="delete-account"),
]
