from rest_framework.viewsets import ModelViewSet
from .models import Psicologo
from .serializers import PsicologoSerializer

class PsicologoViewSet(ModelViewSet):
    queryset = Psicologo.objects.all()
    serializer_class = PsicologoSerializer