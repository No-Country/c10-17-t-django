from django.urls import path
from .views import *

urlpatterns = [
    path('create-site/', CreateSite.as_view(), name='Create Site'),
    path('add-photo-site/', AddPhotoSite.as_view(), name='Add Photo Site'),
    path('get-site/', ShowSite.as_view(), name='Get Site'),
    path('list-photo-site/', ShowListPhoto.as_view(), name='Photos Site'),
    path('update-site/<str:id_site>/', UpdateSite.as_view(), name='Update Site'),
    path('list-site', ShowListSite.as_view(), name='List Site'),
    path('list-guide-site', ShowGuideSite.as_view(), name='List Guide Site')
]