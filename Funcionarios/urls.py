from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfessorViewSet, DisciplinaViewSet, ReservaAmbienteViewSet, ProfessorDisciplinaViewSet, LoginView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Professores",
        default_version='v1',
        description="Documentação da API de Professores e Disciplinas",
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# Configuração do roteador
router = DefaultRouter()
router.register(r'professores', ProfessorViewSet, basename="professores")
router.register(r'disciplinas', DisciplinaViewSet, basename="disciplinas")
router.register(r'reservas', ReservaAmbienteViewSet, basename="reservas")
router.register(r'materias', ProfessorDisciplinaViewSet, basename="materias")

# URLs da aplicação
urlpatterns = [
    path('logar/', LoginView.as_view(), name="login"),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
]
