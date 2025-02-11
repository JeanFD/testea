from django.urls import path
from . import views
# from .api import viewsets
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# route = routers.DefaultRouter()
# route.register(r'animal', animalviewswts.AnimalViewSet, basename='Animal')
# route.register(r'usuario', animalviewswts.UsuarioViewSet, basename='Usuario')

urlpatterns = [
    path('', views.index, name='index'),
    # path('doacoes', views.doacoes, name='doacoes'),
    # path('saiba_mais', views.saiba_mais, name='saiba_mais'),
    # path('contato', views.contato, name='contato'),
    # path('login/', views.login_view, name='login'),
    # path('logout/', views.logout_view, name='logout'),
    # path('cadastro/', views.cadastro, name='cadastro'),
    # path('add-animal/', views.add_animal, name='add_animal'),
    # path('excluir-animal/', views.excluir_animal, name='excluir_animal'),



    # path('api/animais/', viewsets.AnimalListCreateView.as_view(), name='api-animais'),
    # path('api/animais/<int:pk>/', viewsets.AnimalDetailView.as_view(), name='api-animal-detail'),
    # path('api/cadastro/', viewsets.CadastroUsuarioView.as_view(), name='api-cadastro'),
    # # path('api/desenvolvedores/', views.DesenvolvedorListView.as_view(), name='api-desenvolvedores'),
    
    # # Autenticação JWT
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
