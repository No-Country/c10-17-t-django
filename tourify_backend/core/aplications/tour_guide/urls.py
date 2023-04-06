from django.urls import path
from .views import *

urlpatterns = [
    #Crud Contact
    path('create-guide/',RegisterGuide.as_view()),
    path('show-contact/',ShowPersonalContactGuide.as_view()),
    path('update-contact/<pk>/',UpdatePersonalContactGuide.as_view()),
    path('delete-contact/<pk>/',DeletePersonalContactGuide.as_view()),
    #Crud Certifications
    path('list-certifications/',ListCertification.as_view()),
    path('create-certification/',CreateCertification.as_view()),
    path('update-certification/<pk>/',UpdateCertification.as_view()),
    path('delete-certification/<pk>/',DeleteCertification.as_view()),
]
