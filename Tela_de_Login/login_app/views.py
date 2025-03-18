from django.shortcuts import render, redirect
from django.contrib import messages
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

        # Criar novo usuário e armazenar senha com hashing
        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.set_senha(senha) 
        novo_usuario.save()

        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('/')  

    return render(request, "Cadastro/cadastro.html")


# View para fazer login
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # Verifica se o usuário existe no banco de dados
        usuario = Usuario.objects.filter(email=email).first()

        if usuario and usuario.verificar_senha(senha):
            messages.success(request, f"Bem-vindo, {usuario.nome}!")
            return redirect('/')
        else:
            messages.error(request, "Erro: Email ou senha inválidos!")

    return render(request, "Cadastro/login.html")
