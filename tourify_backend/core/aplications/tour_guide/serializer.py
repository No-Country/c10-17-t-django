from rest_framework.serializers import ModelSerializer
from aplications.authentication.models import CustomUser

from .models import Guide,Certification,Review_Guide,Report
from aplications.tourist_spot.models import Favorite_site

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('name', 'last_name', 'age', 'email')


class GuideSerializer(ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'

class CertificationSerializer(ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class GuideContactSerializer(ModelSerializer):
    user = CustomUserSerializer(read_only=True, source='id_user')
    class Meta:
        model = Guide
        fields = ('user','phone','address','country')

class ReviewGuideSerializer(ModelSerializer):
    class Meta:
        model = Review_Guide
        fields = '__all__'

class SavedFavoriteSiteSerializer(ModelSerializer):
    class Meta:
        model = Favorite_site
        fields = '__all__'

class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'user', 'reason', 'created_at']