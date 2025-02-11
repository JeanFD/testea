from .models import Animal, Desenvolvedor
# from .forms import CustomLoginForm, AnimalForm, CustomUsuarioForm 
# from django.contrib.auth import login, logout
# from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages

def index(request):
    is_voluntario = request.user.groups.filter(name='Voluntários').exists() if request.user.is_authenticated else False
    animais = Animal.objects.order_by('?').all()
    return render(request, 'doguinhos.html', {'animais': animais, 'is_voluntario': is_voluntario})

# def doacoes(request):
#     return render(request, 'doacoes.html')

# def saiba_mais(request):
#     return render(request, 'saiba_mais.html')

# def contato(request):
#     desenvolvedores = Desenvolvedor.objects.all()
#     return render(request, 'contato.html', {'voluntarios': desenvolvedores})

# def login_view(request):
#     if request.method == 'POST':
#         form = CustomLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')  # Redirecione para a página inicial ou protegida
#         else:
#             messages.error(request, "Login inválido")
#     else:
#         form = CustomLoginForm()
#     return render(request, 'login.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('index')

# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def add_animal(request):
#     if request.method == 'POST':
#         form = AnimalForm(request.POST, request.FILES)
#         if form.is_valid():
#             animal = form.save(commit=False)
#             animal.criado_por = request.user
#             animal.save()
#             return redirect('index')
#     else:
#         form = AnimalForm()
#     return render(request, 'add_animal.html', {'form': form})

# @login_required
# @user_passes_test(lambda u: u.is_staff)
# def excluir_animal(request):
#     if request.method == 'POST':
#         animal_id = request.POST.get('animal_id')
#         animal = get_object_or_404(Animal, id=animal_id)
#         animal.delete()
#         return redirect('index')


# def cadastro(request):
#     if request.method == 'POST':
#         form = CustomUsuarioForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = CustomUsuarioForm()
    
#     return render(request, 'cadastro.html', {'form': form})

