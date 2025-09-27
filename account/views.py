from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages  # Para mostrar erros
from core.views.colaborador_views import home  # ou sua url 'home'

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(home)  # redireciona para a home
        else:
            messages.error(request, 'Usuário ou senha incorretos')

    return render(request, 'account/pages/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')

#         user = User.objects.create_user(username=username, password=password, email=email)
#         user.save()
#         return redirect('login')
#     return render(request, 'account/register.html')

# def password_reset_request(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         # Logic to handle password reset request
#         # e.g., generate token, send email, etc.
#     return render(request, 'account/password_reset.html')