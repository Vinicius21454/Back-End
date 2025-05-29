from rest_framework import serializers
from .models import Usuario, Disciplina, ReservaAmbiente, Reserva, ProfessorDisciplina
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ReservaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAmbiente
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva  # Corrigido de "models = Reserva" para "model = Reserva"
        fields = '__all__'

class ProfessorDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessorDisciplina
        fields = '__all__'

class LoginSerializer(TokenObtainPairSerializer):
    class Meta:
        model = Usuario  # Corrigido de "models = Usuario" para "model = Usuario"
        fields = '__all__'
