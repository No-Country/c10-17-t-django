from django.db import models
from aplications.authentication.models import CustomUser



from .managers import TourGuideManager,CertificationsManager,ReviewsGuideManager
STATE_GUIDE = (('1','ACTIVO'),('2','INACTIVO'),('3','BLOQUEADO'))

# Create your models here.
class Guide(models.Model):
    dni = models.CharField(max_length=150,null=False,blank=False,unique=True,primary_key=True)
    phone = models.CharField(max_length=50,blank=False,null=False)
    address = models.CharField(max_length=50,blank=False,null=False)
    country = models.CharField(max_length=20,blank=False,null=False)
    postal_code = models.CharField(max_length=50,blank=False,null=False)
    state = models.CharField(max_length=10,choices=STATE_GUIDE,blank=False,null=False)
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    objects = TourGuideManager()


class Certification(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    institute = models.CharField(max_length=50,null=False,blank=False)
    broadcast_date = models.DateField(null=False,blank=False)
    link = models.CharField(max_length=150,null=False,blank=False)
    dni = models.ForeignKey(Guide, on_delete=models.CASCADE)

    objects = CertificationsManager()

class Review_Guide(models.Model):
    calification = models.FloatField(null=False,blank=False)
    comment = models.TextField(null=False,blank=False)
    id_user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    dni = models.ForeignKey(Guide, on_delete=models.CASCADE)

    objects = ReviewsGuideManager()
    
class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reports')
    reason = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)