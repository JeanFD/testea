from django.db import models
from stdimage.models import StdImageField
from django.contrib.auth.models import AbstractUser, BaseUserManager

class Pessoas(models.Model):
    nome = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default = '')
    telefone = models.CharField(max_length=15, default = 0)
    img = StdImageField('Fotos', upload_to='fotos_voluntarios/', variations={'thumb': (1080, 1080, True)})
    class Meta:
        abstract = True
    def __str__(self):
        return self.nome
    
class Desenvolvedor(Pessoas):
    linkedin = models.CharField(max_length=100, default='')
    class Meta:
        verbose_name = "Desenvolvedor"
        verbose_name_plural = "Desenvolvedores"

class Raca(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Raça")

class Animal(models.Model):
    nome = models.CharField(max_length=20)
    raca = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    idade = models.IntegerField()
    vacinado = models.BooleanField(default=False)
    descricao = models.TextField(max_length=56)
    descricao_completa = models.TextField()
    local = models.CharField(max_length=100, default="")
    foto = StdImageField('Fotos', upload_to='fotos_animais/', variations={'thumb': (1080, 1080, True)}, blank=True)
    criado_por = models.ForeignKey('CustomUsuario', on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = "Doguinho"
        verbose_name_plural = "Doguinhos"
    def __str__(self):
        return self.nome

class UsuarioManager(BaseUserManager):
    
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório!')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        # is_staff = models.BooleanField('Membro da equipe', default = False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)
    
class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone (DDD do país e do estado)', max_length=15)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email
    
    objects = UsuarioManager()

    