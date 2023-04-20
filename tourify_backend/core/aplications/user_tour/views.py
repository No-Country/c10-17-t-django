from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FollowUpSerializer

from aplications.authentication.models import CustomUser,FollowUp


# Create your views here.
class FollowUser(APIView):
    def post(self, request):
        username_following = self.request.data["username_following"]
        username_follower = self.request.data["username_follower"]
       
        # Verifica que el usuario a seguir existe
        user_following = get_object_or_404(CustomUser, username=username_following)
        user_follower = get_object_or_404(CustomUser, username=username_follower)

        # Verifica que el usuario no esté siguiendo a sí mismo
        if user_following == user_follower:
            return Response({"error": "No puedes seguirte a ti mismo"}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica que no se esté siguiendo ya a este usuario
        if FollowUp.objects.filter(id_folower=user_follower, id_folowing=user_following).exists():
            return Response({"error": "Ya estás siguiendo a este usuario"}, status=status.HTTP_400_BAD_REQUEST)

        # Crea la instancia de seguimiento y la guarda en la base de datos
        follow_up = FollowUp(id_folower=user_follower, id_folowing=user_following)
        follow_up.save()

        return Response({"success": f"Ahora estás siguiendo a {user_following.username}"}, status=status.HTTP_201_CREATED)

class UnFollowUser(APIView):
    def post(self, request):
        username_following = self.request.data["username_following"]
        username_follower = self.request.data["username_follower"]
        

        # Verifica que el usuario a dejar de seguir existe
        user_following = get_object_or_404(CustomUser, username=username_following)
        user_follower = get_object_or_404(CustomUser, username=username_follower)

        # Verifica que se esté siguiendo ya a este usuario
        follow_up = FollowUp.objects.filter(id_folower=user_follower, id_folowing=user_following)
        if not follow_up.exists():
            return Response({"error": "No estás siguiendo a este usuario"}, status=status.HTTP_400_BAD_REQUEST)

        # Elimina la instancia de seguimiento de la base de datos
        follow_up.delete()

        return Response({"success": f"Ahora ya no estás siguiendo a {user_following.username}"}, status=status.HTTP_200_OK)

class ListFollowings(APIView):
    def get(self, request):
        username  = self.request.query_params.get('username',None)
        # Verifica que el usuario exista
        user = get_object_or_404(CustomUser, username=username)

        # Recupera todos los usuarios que está siguiendo este usuario
        following = FollowUp.objects.filter(id_folowing=user)
        serializer = FollowUpSerializer(following, many=True)

        return Response(serializer.data)

class ListFollowers(APIView):
    def get(self, request):
        username  = self.request.query_params.get('username',None)
        # Verifica que el usuario exista
        user = get_object_or_404(CustomUser, username=username)

        # Recupera todos los usuarios que están siguiendo a este usuario
        followers = FollowUp.objects.filter(id_folower=user)
        serializer = FollowUpSerializer(followers, many=True)

        return Response(serializer.data)