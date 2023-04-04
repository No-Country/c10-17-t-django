from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
STATE_GS = (('A','Activo'),('I','Inactivo'),('S','Suspendido'))
QUALIFICATION = (('M','Malo'),('R','Regular'),('B','Bueno'),('MB','Muy bueno'),('E','Excelente'))

class Site (models.Model):
    id_site= models.CharField(max_length=5, primary_key=True, null=False, unique=True)
    name= models.CharField(max_length=50, blank=False, null=False)
    description= models.CharField(max_length=300 ,blank=False, null=False)
    latitude= models.CharField(max_length=10,blank=False, null=False)
    lenght= models.CharField(max_length=10,blank=False, null=False)
    location= models.CharField(max_length=50,blank=False, null=False)
    province= models.CharField(max_length=50,blank=False, null=False)
    country= models.CharField(max_length=50,blank=False, null=False)
    budget= models.FloatField(validators=[MinValueValidator(0)] , blank=False, null=False)
    validation= models.BooleanField(default=False)

class Photo_site (models.Model):
    name= models.CharField(max_length=50, blank=False, null=False)
    description= models.CharField(max_length=100, blank=False, null=False)
    upload_date = models.DateTimeField(auto_now=True,blank=False, null=False)
    link = models.CharField(max_length=100, blank=False, null=False)
    id_site= models.ForeignKey(Site, on_delete=models.CASCADE)

class Guide_site (models.Model):
    date_register= models.DateTimeField(auto_now=True, blank=False, null=False)
    date_update_site= models.DateTimeField(blank=True, null= True)
    description_update= models.CharField(max_length=100, blank=True, null=True)
    state= models.CharField(max_length=30, choices= STATE_GS)
    id_site= models.ForeignKey(Site, on_delete=models.CASCADE)
    dni= models.ForeignKey() #REQUIERE DEL MODELO GUIA

class Display (models.Model):
    nro_view= models.Model(max_length=5, primary_key=True, null=False, unique=True)
    date_view= models.DateTimeField(auto_now=True, blank=False, null= False)
    id_user= models.ForeignKey() #REUIERE DEL MODELO USUARIO
    id_site= models.ForeignKey(Site, on_delete=models.CASCADE)

class Visit_site (models.Model):
    visit_number= models.Model(max_length=5, primary_key=True, null=False, unique=True)
    date_visitdate_view= models.DateTimeField(auto_now=True, blank=False, null= False)
    qualification= models.CharField(max_length=10, choices=QUALIFICATION)
    trasport= models.FloatField(validators=[MinValueValidator(0)] , blank=False, null=False)
    housing= models.FloatField(validators=[MinValueValidator(0)] , blank=False, null=False)
    meal= models.FloatField(validators=[MinValueValidator(0)] , blank=False, null=False)
    coment= models.CharField(max_length=300, blank=True, null=True)
    recomentadion= models.CharField(max_length=100, blank=True, null=True)
    id_user= models.ForeignKey() #REUIERE DEL MODELO USUARIO
    id_site= models.ForeignKey(Site, on_delete=models.CASCADE)

class Photo_visit (models.Model):
    name= models.CharField(max_length=50, blank=False, null=False)
    link= models.CharField(max_length=100, blank=False, null=False)
    visit_number= models.ForeignKey(Visit_site, on_delete=models.CASCADE)
