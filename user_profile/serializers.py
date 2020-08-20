from rest_framework.serializers import ModelSerializer
from .models import UserProfile
from psicologo.serializers import PsicologoSerializer

class UserSerializer(ModelSerializer):
    psicologo = PsicologoSerializer(many=False)
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','email', 'username','psicologo','password','active', 'is_staff')
