from rest_framework.serializers import ModelSerializer
from .models import Psicologo
from formacao.serializers import FormacaoSerializer

class PsicologoSerializer(ModelSerializer):

    formacao = FormacaoSerializer(many=True)

    class Meta:
        model = Psicologo
        fields=('numCRP','formacao')