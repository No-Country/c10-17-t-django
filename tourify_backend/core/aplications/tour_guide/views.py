from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,ListAPIView,DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Guide,Certification,Review_Guide
from .serializer import GuideSerializer,CertificationSerializer,GuideContactSerializer,ReviewGuideSerializer
# Create your views here.

#Crud guides
class RegisterGuide(CreateAPIView):
    model = Guide
    serializer_class = GuideSerializer

class ShowPersonalContactGuide(APIView):
    serializer_class = GuideSerializer

    def get(self,request):
        user_guide = self.request.query_params.get('id_user')
        contact_info = Guide.objects.search_user_guide(user_guide)
        serializer_info = GuideContactSerializer(contact_info)

        return Response(serializer_info.data,status=status.HTTP_200_OK)

class UpdatePersonalContactGuide(RetrieveUpdateAPIView):
    serializer_class = GuideContactSerializer
    queryset = Guide.objects.get_all_tour_guide()

class DeletePersonalContactGuide(DestroyAPIView):
    serializer_class = GuideContactSerializer
    queryset =  Guide.objects.get_all_tour_guide()

#Crud Certification
class CreateCertification(CreateAPIView):
    model = Certification
    serializer_class = CertificationSerializer

class ListCertification(ListAPIView):
    serializer_class = CertificationSerializer
    queryset = Certification.objects.get_all_certifications()

class UpdateCertification(RetrieveUpdateAPIView):
    serializer_class = CertificationSerializer
    queryset = Certification.objects.get_all_certifications()

class DeleteCertification(DestroyAPIView):
    serializer_class = CertificationSerializer
    queryset = Certification.objects.get_all_certifications()

#Crear Reseña del lugar turistico
class CreateReviewGuide(CreateAPIView):
    model = Review_Guide
    serializer_class = ReviewGuideSerializer 

    

