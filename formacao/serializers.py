from rest_framework.serializers import ModelSerializer
from .models import Formacao


class FormacaoSerializer(ModelSerializer):
    class Meta:
        model = Formacao
        fields = ('instituicao','status','concluido','titulo')