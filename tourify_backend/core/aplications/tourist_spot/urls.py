from django.urls import path
from .views import *
from django.urls import path
from .views import *

urlpatterns = [
    path('create-site/', CreateSite.as_view(), name='create_site'),
    path('add-photo-site/', AddPhotoSite.as_view(), name='add_photo_site'),
    path('get-site/', ShowSite.as_view(), name='get_site'),
    path('list-photo-site/', ShowListPhoto.as_view(), name='photos_site'),
    path('update-site/<str:id_site>/', UpdateSite.as_view(), name='update_site'),
    path('list-site/', ShowListSite.as_view(), name='list_site'),
    path('list-guide-site/', ShowGuideSite.as_view(), name='list_guide_site'),
    path('list-favorite-site/', ShowFavoriteSite.as_view(), name= 'list_favorite_site'),
    path('list-visit-site/', ShowVisitSite.as_view(), name= 'list_visit_site'),
    path('photo-visit/',ShowPhotoVisit.as_view(), name='list_photo_visit'),
    path('bookmark/<str:id_user>/<str:id_site>/', BookmarkFavoriteSite.as_view(), name='bookmark_favorite_site'),
    path('search-name/',SearchSiteByName.as_view(), name='search_site_by_name'),
    path('search-budget/',SearchSiteByBudget.as_view(), name='search_site_by_budget'),
    path('search-province/',SearchSiteByProvince.as_view(), name='search_site_by_province')
]