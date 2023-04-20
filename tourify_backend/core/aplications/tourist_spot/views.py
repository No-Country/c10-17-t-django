from django.shortcuts import get_object_or_404, render
from .models import Site, Guide_site, Photo_site
from .serializers import SiteSerializer, GuideSiteSerializer, PhotoSiteSerializer
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
        validation= self.request.query_params.get('validation')
        valit_site= Site.objects.filter(validation=validation)
        list_site= SiteSerializer(valit_site, many=True)

        if len(list_site.data)!=0:
            return Response(list_site.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron lugares para mostrar"},status=status.HTTP_204_NO_CONTENT)

#LISTAR GUIAS DE UN LUGAR TURISTICO
class ShowGuideSite(APIView):
    def get(self, request):
        id_site= self.request.query_params.get('id_site')
        guide_site= Guide_site.objects.filter(id_site=id_site) #No mostrar aquellos Desabilitados
        list_guide= GuideSiteSerializer(guide_site, many=True)

        if len(list_guide.data)!=0:
            return Response(list_guide.data, status=status.HTTP_200_OK)
        return Response({"message":"No se encontraron lugares para mostrar"},status=status.HTTP_204_NO_CONTENT)