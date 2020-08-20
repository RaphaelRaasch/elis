from django.contrib.auth.models import User
from django.db import models

from psicologo.models import Psicologo


class UserProfile(User):
    active = models.BooleanField('Active', default=False)
    created = models.DateField(auto_now_add=True)
    psicologo = models.ForeignKey(Psicologo, on_delete=models.CASCADE, blank=True, null=True)
