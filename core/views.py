from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Pessoal
from .serializers import PessoalSerializer

def home(request):
    # Se você já alterou essa view no exercício anterior, mantenha como está
    return render(request, 'portfolio/home.html')

class PerfilDetail(generics.RetrieveUpdateAPIView):
    """
    GET /api/perfil/ → Retorna o perfil do usuário logado
    PUT /api/perfil/ → Atualiza o perfil completo
    PATCH /api/perfil/ → Atualiza parcialmente
    """

    serializer_class = PessoalSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Em vez de buscar pelo pk da URL, busca pelo usuário logado.
        Se o perfil não existir, cria um vazio automaticamente.
        """
        perfil, created = Pessoal.objects.get_or_create(
            usuario=self.request.user,
            defaults={
                'nome': self.request.user.username,
            },
        )
        return perfil
    