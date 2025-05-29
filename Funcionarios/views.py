from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS
from .models import Usuario, Reserva, Disciplina, ProfessorDisciplina
from .serializers import UsuarioSerializer, DisciplinaSerializer, ReservaAmbienteSerializer, ReservaSerializer, ProfessorDisciplinaSerializer
from .permissions import IsGestor, IsProfessorReadOnly
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status


class ProfessorViewSet(viewsets.ModelViewSet):
    """
    API para gerenciamento de professores.
    """
    queryset = Usuario.objects.filter(autorizacoes="C")  # Ajustado para listar apenas professores
    serializer_class = UsuarioSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            permission_classes = [IsProfessorReadOnly | IsGestor]
        else:
            permission_classes = [IsGestor]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(operation_description="Lista todos os professores cadastrados.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cria um novo professor no sistema.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Atualiza um professor pelo ID.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Remove um professor pelo ID.")
    def destroy(self, request, *args, **kwargs):
        professor = self.get_object()
        professor.delete()
        return Response({"mensagem": "Professor deletado com sucesso"}, status=status.HTTP_204_NO_CONTENT)


class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    API para gerenciamento de disciplinas.
    """
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]

    @swagger_auto_schema(operation_description="Lista todas as disciplinas cadastradas.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cria uma nova disciplina no sistema.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Atualiza uma disciplina pelo ID.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Remove uma disciplina pelo ID.")
    def destroy(self, request, *args, **kwargs):
        disciplina = self.get_object()
        disciplina.delete()
        return Response({"mensagem": "Disciplina deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)


class ReservaAmbienteViewSet(viewsets.ModelViewSet):
    """
    API para gerenciamento de reservas de ambiente.
    """
    queryset = Reserva.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsGestor]

    @swagger_auto_schema(operation_description="Lista todas as reservas cadastradas.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cria uma nova reserva no sistema.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Atualiza uma reserva pelo ID.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Remove uma reserva pelo ID.")
    def destroy(self, request, *args, **kwargs):
        reserva = self.get_object()
        reserva.delete()
        return Response({"mensagem": "Reserva deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)


class ReservaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API para visualizar reservas, acesso apenas autenticado.
    """
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        return Reserva.objects.filter(usuario=usuario)

    @swagger_auto_schema(operation_description="Lista todas as reservas cadastradas.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class DisciplinaUsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API para listar disciplinas associadas a um usuário autenticado.
    """
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        return Disciplina.objects.filter(professor=usuario)


class ProfessorDisciplinaViewSet(viewsets.ModelViewSet):
    """
    API para gerenciamento da relação entre professores e disciplinas.
    """
    queryset = ProfessorDisciplina.objects.all()
    serializer_class = ProfessorDisciplinaSerializer
    permission_classes = [IsGestor]

    @swagger_auto_schema(operation_description="Lista todas as associações entre professores e disciplinas.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Cria uma nova associação entre professor e disciplina.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Atualiza uma associação entre professor e disciplina pelo ID.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Remove uma associação entre professor e disciplina pelo ID.")
    def destroy(self, request, *args, **kwargs):
        associacao = self.get_object()
        associacao.delete()
        return Response({"mensagem": "Associação deletada com sucesso"}, status=status.HTTP_204_NO_CONTENT)


class LoginView(TokenObtainPairView):
    """
    Endpoint de login para obter tokens JWT.
    """
    serializer_class = TokenObtainPairSerializer
    permission_classes = [AllowAny]
