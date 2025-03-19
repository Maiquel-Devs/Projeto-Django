from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Usuario

# View para cadastrar um usuário
def cadastro(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Verifica se o email já está cadastrado
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "Erro: Email já cadastrado!")
            return redirect('cadastro')

        # Criar novo usuário e armazenar senha com hashing correto
        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.set_senha(senha)  
        novo_usuario.save()

        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('login')  
    
    return render(request, "Cadastro/login.html")

# View para fazer login
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        usuario = Usuario.objects.filter(email=email).first()

        if usuario and usuario.verificar_senha(senha):
            django_login(request, usuario)
            next_url = request.GET.get('next', 'home')  
            return redirect(next_url)
        else:
            messages.error(request, "Erro: Email ou senha inválidos!")

    return render(request, "Cadastro/login.html")

# Pagina inicial do usuario logado
@login_required
def home(request):
    # Recupera o usuário logado
    usuario_logado = request.user  
    return render(request, 'Cadastro/home.html', {'usuario': usuario_logado})
