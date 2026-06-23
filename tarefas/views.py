from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Tarefa
from .serializers import TarefaSerializer


# ─── Estilo 1: Function-Based Views ───
@api_view(['GET', 'POST'])
def tarefa_list_create_fbv(request):
    pass

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def tarefa_detail_fbv(request, pk):
    pass


# ─── Estilo 2: Class-Based Views ───
class TarefaListCreateAPIView(APIView):
    pass

class TarefaDetailAPIView(APIView):
    pass


# ─── Estilo 3: Generic Views ───
class TarefaListCreate(generics.ListCreateAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):       
        return Tarefa.objects.filter(responsavel=self.request.user)

    def perform_create(self, serializer): 
        serializer.save(responsavel=self.request.user)


class TarefaDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TarefaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):         
        return Tarefa.objects.filter(responsavel=self.request.user)