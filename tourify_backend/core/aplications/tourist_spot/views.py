from django.shortcuts import get_object_or_404, render
from .models import Site, Guide_site, Photo_site, Favorite_site, Visit_site, Photo_visit
from .serializers import *
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

#REGISTRAR UN LUGAR TURISTICO
class CreateSite(CreateAPIView):
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.isvalid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(
                    {"message":"Se ha creado el lugar correctamente"},
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"message": "Ocurrio un error al crear el lugar: " + str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
#AGREGAR FOTOS PARA UN LUGAR TURISTICO
class AddPhotoSite(CreateAPIView):
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.isvalid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(
                {"message": "Imagen agregada correctamente"}
            )
        except Exception as e:
            return Response(
                {"message": "Ocurrio un error al agregar la imagen: "+ str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

#MOSTRAR INFORMACION DE UN LUGAR TURISTICO 
class ShowSite(APIView):
    def get(self, request):
        id_site = self.request.query_params.get('id_site')
        turist_site = Site.objects.filter(id_site=id_site)
        if( turist_site is not None):  
            turist_site_serializer = SiteSerializer(turist_site)
            return Response(turist_site_serializer.data,status=status.HTTP_200_OK)

        return Response({"message":"Error al buscar el lugar turistico"},status=status.HTTP_404_NOT_FOUND)
    
#MOSTRAR FOTOS DE UN LUGAR TURISTICO
class ShowListPhoto(APIView):
    def get(self,request):
        id_site= self.request.query_params.get('id_site')
        photo_site = Photo_site.objects.filter(id_site=id_site)
        list_photo = PhotoSiteSerializer(photo_site, many=True)

        if len(list_photo.data)!=0:
            return Response(list_photo.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron imagenes para mostrar"},status=status.HTTP_204_NO_CONTENT)

#MODIFICAR INFORMACION DE UN LUGAR TURISTICO  
class UpdateSite(UpdateAPIView):

    serializer_class= SiteSerializer

    def update(self, request, id_site):
        patient = get_object_or_404(Site, id_site=id_site)
        serializer = self.get_serializer(patient, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Cambios guardados correctamente"})
    
#LISTAR LUGARES TURISTICOS
class ShowListSite(APIView):
    def get(self, request):

        valit_site= Site.objects.filter(validation=True)
        list_site= SiteSerializer(valit_site, many=True)

        if len(list_site.data)!=0:
            return Response(list_site.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron lugares para mostrar"},status=status.HTTP_204_NO_CONTENT)
    
#BUSCAR LUGARES SEGUN EL NOMBRE
class SearchSiteByName(APIView):
    def get(self,request):
        search_query=self.request.query_params.get('q')
        if search_query:
            valid_site=Site.objects.filter(validation=True, name__icontains=search_query)
        list_site=SiteSerializer(valid_site, many=True)
        if len(list_site.data)!=0:
            return Response(list_site.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron coincidencias en el nombre"},status=status.HTTP_204_NO_CONTENT)
        
#BUSCAR LUGARES SEGUN EL PRESUPUESTO
class SearchSiteByBudget(APIView):
    def get(self,request):
        min_budget = request.query_params.get('min_budget')
        max_budget = request.query_params.get('max_budget')

        valid_site=Site.objects.filter(validation=True, budget__gte=min_budget, budget__lte=max_budget)
        list_site=SiteSerializer(valid_site, many=True)
        if len(list_site.data)!=0:
            return Response(list_site.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron lugares segun el presupuesto ingresado"},status=status.HTTP_204_NO_CONTENT)

#BUSCAR LUGARES SEGUN LA PROVINCIA
class SearchSiteByProvince(APIView):
    def get(self,request):
        search_query= self.request.query_params.get('q')
        if search_query:
            valid_site=Site.objects.filter(validation=True, province__icontains=search_query)
        list_site=SiteSerializer(valid_site, many=True)
        if len(list_site.data)!=0:
            return Response(list_site.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron lugares cercanos a tu ubicacion"},status=status.HTTP_204_NO_CONTENT)

#LISTAR GUIAS DE UN LUGAR TURISTICO
class ShowGuideSite(APIView):
    def get(self, request):
        id_site= self.request.query_params.get('id_site')
        guide_site= Guide_site.objects.filter(id_site=id_site, state=not('S','Suspendido')) #No mostrar aquellos suspendidos
        list_guide= GuideSiteSerializer(guide_site, many=True)

        if len(list_guide.data)!=0:
            return Response(list_guide.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron guias para el lugar seleccionado"},status=status.HTTP_204_NO_CONTENT)
    
#LISTAR LUGARES FAVORITOS
"""class ShowFavoriteSite(APIView):
    def get(self,request):
        id_user = self.request.query_params.get('id_user')
        favorite_site= Favorite_site.objects.filter(id_user=id_user)
        list_favorite= FavoriteSiteSerializer(favorite_site, many=True)

        if len(list_favorite.data)!=0:
            return Response(list_favorite.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontaron lugares marcados como favoritos"})"""
    
class ShowFavoriteSite(APIView):
    def get(self,request):
        id_user = self.request.query_params.get('id_user')
        favorite_site= Favorite_site.objects.filter(id_user=id_user)
        sites = [site.id_site for site in favorite_site]
        list_site = SiteSerializer(sites, many=True)
        if len(list_site.data) !=0:
            return Response(list_site.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron lugares marcados como favoritos"})


#MOSTRAR RESEÑAS DE UN LUGAR TURISTICO
"""class ShowReviewSite(APIView):
    def get(self,request):
        id_site= self.request.query_params.get('id_side')
        visit_site= Visit_site.objects.filter(id_side=id_side)
        list_visit= VisitSiteSerializer(visit_site, many=True)

        if len(list_visit.data)!=0:
            return Response(list_visit.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron lugares visitados"})"""


#MOSTRAR LUGARES VISITADOS
class ShowVisitSite(APIView):
    def get(self,request):
        id_user= self.request.query_params.get('id_user')
        visit_site= Visit_site.objects.filter(id_user=id_user)
        sites=[site.id_site for site in visit_site]
        list_site = SiteSerializer(sites, many=True)
        if len(list_site.data) !=0:
            return Response(list_site.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron lugares que hallas visitado"})
    
#MOSTRAR FOTOS DE UNA VISITA TURISTICO
class ShowPhotoVisit(APIView):
    def get(self,request):
        visit_number= self.request.query_params.get('visit_number')
        photo_site = Photo_visit.objects.filter(visit_number=visit_number)
        list_photo = PhotoVisitSerializer(photo_site, many=True)

        if len(list_photo.data)!=0:
            return Response(list_photo.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron imagenes para mostrar"},status=status.HTTP_204_NO_CONTENT)

#DENTIFICAR UN LUGAR FAVORITO
class BookmarkFavoriteSite(APIView):
    def get(self,request,id_user, id_site):
        favorite_site = Favorite_site.objects.filter(id_user=id_user,id_site=id_site)
        if favorite_site.exists():
            return Response(True)
        return Response(False)