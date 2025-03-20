from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Usuario  # Importa o modelo personalizado

# View de Login
def login_view(request):
    if request.method == "POST":
        username = request.POST["usuario"]
        password = request.POST["senha"]

        # Busca usuário na tabela personalizada no models
        try:
            user = Usuario.objects.get(usuario=username, senha=password)
            request.session['usuario_id'] = user.id  # Salva na sessão
            return redirect('home')  
        except Usuario.DoesNotExist:
            return render(request, 'Cadastro/login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'Cadastro/login.html')

# View de Cadastro
def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST['usuario']
        password = request.POST['senha']

        # Verifica se já existe um usuário com o mesmo nome de usuário
        if Usuario.objects.filter(usuario=username).exists():
            error_message = "Usuário já existe. Escolha outro nome de usuário."
            return render(request, 'Cadastro/login.html', {'error': error_message})

        # Criar o novo usuário na tabela personalizada no models
        user = Usuario(usuario=username, senha=password)
        user.save()
        print(f"Usuário {username} salvo na tabela Usuario.")

        return redirect('login')  

    return render(request, 'Cadastro/login.html')

# View de Logout
def logout_view(request):
    request.session.flush()  
    return redirect('login') 

# View de Home
def home_view(request):
    if 'usuario_id' not in request.session:
        return redirect('login')  

    usuario = Usuario.objects.get(id=request.session['usuario_id'])  #
    return render(request, 'Cadastro/home.html', {'usuario': usuario})
