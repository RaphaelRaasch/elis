from rest_framework.viewsets import ModelViewSet
from .models import Formacao
from .serializers import FormacaoSerializer


class FormacaoView(ModelViewSet):
    queryset = Formacao.objects.all()
    serializer_class = FormacaoSerializer
