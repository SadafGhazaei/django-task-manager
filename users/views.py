from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class LogoutView(LoginRequiredMixin, View):
    def post(self, request):
        logout(request)
        return redirect('home')
