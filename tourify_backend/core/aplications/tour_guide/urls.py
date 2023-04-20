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
    #Review Guide
    path('create-review-guide/',CreateReviewGuide.as_view()),
    #Show All Review Guide
    path('show-all-review-guide/',ShowReviewGuide.as_view()),
    #Save Visite Site
    path('save-visite-site/',SavedPostView.as_view()),
    #Report user
    path('report-user/',ReportUserView.as_view()),
    #Create Visite Site
    path('create-visit-site/',CreateVisiteSite.as_view()),

]
