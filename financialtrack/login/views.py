from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

class LoginView(generic.View):
    def get(self, request):
        context = {'login':True}
        return render(request, 'login.html', context)

    def post(self, request):
        user = authenticate(request,
                            username=request.POST.get('username'),
                            password = request.POST.get('password'))

        if user is not None:
            auth_login(request, user)
            return redirect(request.get_full_path().split('=')[-1])

        else:
            return redirect(request.get_full_path())
