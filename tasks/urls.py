from django.urls import path
from . import views
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path('api/tasks/', TaskListCreateView.as_view(), name='api-task-list'),
    path('api/tasks/<int:pk>/', views.TaskDetailView.as_view(), name='api-task-detail'),
    
    path('', views.TaskListView.as_view(), name='task-list'),
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', views.TaskDetailViewWeb.as_view(), name='task-detail'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),
]