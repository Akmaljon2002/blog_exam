from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        user = authenticate(username = request.POST.get('l'),
                            password = request.POST.get('p'))
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/blog/")

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        if request.POST.get('p') == request.POST.get('o_p'):
            user = User.objects.create_user(
                username = request.POST.get('l'),
                password = request.POST.get('p')
            )
            Muallif.objects.create(
                ism = request.POST.get('ism'),
                yosh = request.POST.get('yosh'),
                kasb = request.POST.get('kasb'),
                user = user
            )
            return redirect('/')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")

class BlogView(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'maqolalar':Maqola.objects.filter(muallif__user=request.user)
            }
            return render(request, 'blog.html', data)
        return redirect("/")

    def post(self, request):
        if request.user.is_authenticated:
            Maqola.objects.create(
                sarlavha = request.POST.get('sarlavha'),
                sana = request.POST.get('sana'),
                mavzu = request.POST.get('mavzu'),
                matn = request.POST.get('matn'),
                muallif = Muallif.objects.get(user=request.user)
            )
            return redirect("/blog/")
        return redirect("/")

class MaqolaView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            data = {
                'maqola':Maqola.objects.get(id=son)
            }
            return render(request, 'maqola.html', data)
        return redirect("/")



