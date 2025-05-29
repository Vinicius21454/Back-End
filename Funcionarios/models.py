from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de usuário
class Usuario(AbstractUser):
    CATEGORIA = [
        ('G', 'Gestor'), 
        ('C', 'Comum')
    ]
    autorizacoes = models.CharField(max_length=1, choices=CATEGORIA, default='C')
    NI = models.CharField(max_length=20, primary_key=True)
    Nome = models.CharField(max_length=255)
    Telefone = models.CharField(max_length=20)
    DataNascimento = models.DateField()
    DataContratacao = models.DateField()
    REQUIRED_FIELDS = ["Nome", "DataNascimento", "DataContratacao"]

    def __str__(self):
        return self.Nome

# Modelo de disciplina
class Disciplina(models.Model):
    Nome = models.CharField(max_length=255)
    Curso = models.CharField(max_length=255)
    CargaHoraria = models.IntegerField()
    Descricao = models.TextField()
    ProfessorResponsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome

# Modelo para associar professores a disciplinas
class ProfessorDisciplina(models.Model):
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.professor.Nome} - {self.disciplina.Nome}"

# Modelo de reserva de ambiente
class ReservaAmbiente(models.Model):
    escolhas = [
        ('Manhã', 'Manhã'), 
        ('Tarde', 'Tarde'), 
        ('Noite', 'Noite')
    ]
    DataInicio = models.DateTimeField()
    DataTermino = models.DateTimeField()
    Periodo = models.CharField(max_length=20, choices=escolhas)
    SalaReservada = models.CharField(max_length=50)
    ProfessorResponsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    DisciplinaAssociada = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva {self.SalaReservada} - {self.DisciplinaAssociada.Nome}"

# Modelo de sala
class Salas(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.nome

# Modelo de reserva
class Reserva(models.Model):
    professor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    sala = models.ForeignKey(Salas, on_delete=models.CASCADE)
    data_reserva = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        return f"Reserva de {self.sala.nome} por {self.professor.Nome} em {self.data_reserva} ({self.horario_inicio} - {self.horario_fim})"
