from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import TaskForm  
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from django.db.models import Q

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        queryset = Task.objects.all()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.all()
    
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        queryset = Task.objects.all().order_by('-created_at')
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        return queryset

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm  
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm  
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
    
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)

class TaskDetailViewWeb(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
    
    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


