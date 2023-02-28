from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

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
        data = {
            'maqolalar':Maqola.objects.all()
        }
        return render(request, 'blog.html', data)
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
        data = {
            'maqola':Maqola.objects.get(id=son)
        }
        return render(request, 'maqola.html', data)





# class Register(View):
#     def post(self, request):
#         if request.POST.get('p') == request.POST.get('cp'):
#             user = User.objects.create_user(
#                 username = request.POST.get('l'),
#                 password = request.POST.get('p')
#             )
#             ism_f = request.POST.get('i')  # Eldor Shomurodov
#             Talaba.objects.create(
#                 ism = ism_f[:ism_f.find(" ")],
#                 familiya = ism_f[ism_f.find(" ")+1:],
#                 st_raqam = request.POST.get('st_r'),
#                 kurs = request.POST.get('k'),
#                 user = user
#             )
#             return redirect('/')

# def post(self, request):
    #     if request.POST.get('p') == request.POST.get('cp'):
    #         User.objects.create_user(
    #             username = request.POST.get('l'),
    #             password = request.POST.get('p')
    #         )
    #     return redirect("/")
    # def get(self, request):
    #     return render(request, 'register.html')
