from django.db import models
from django.contrib.auth.models import AbstractUser

TYPER_USER =(('1','TURISTA'),('2','GUIA'))

STATE_USER =(('1','ACTIVO'),('2','INACTIVO'),('3','BLOQUEADO'))

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)    
    age = models.CharField(max_length=5)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=150,unique=True)
    type_user = models.CharField(max_length=10,choices=TYPER_USER)
    state_user = models.CharField(max_length=10,choices=STATE_USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return f"{self.get_full_name()}"

class FollowUp(models.Model):
    id_folowing = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='following_set')
    id_folower = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='follower_set')
    from_day = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id_folowing', 'id_folower')