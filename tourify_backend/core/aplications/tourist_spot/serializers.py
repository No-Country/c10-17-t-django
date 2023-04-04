from rest_framework.serializers import ModelSerializer
from .models import Site, Photo_site, Guide_site, Display, Visit_site, Photo_visit

class SiteSerializer(ModelSerializer):
    
    class Meta:
        model = Site
        fields = '__all__'
        
class PhotoSiteSerializer(ModelSerializer):
    
    class Meta:
        model = Photo_site
        fields = '__all__'
        
class GuideSiteSerializer(ModelSerializer):
    
    class Meta:
        model = Guide_site
        fields = '__all__'
        
class DisplaySerializer(ModelSerializer):
    
    class Meta:
        model = Display
        fields = '__all__'
        
class VisitSiteSerializer(ModelSerializer):
    
    class Meta:
        model = Visit_site
        fields = '__all__'
        
class PhotoVisitSerializer(ModelSerializer):
    
    class Meta:
        model = Photo_visit
        fields = '__all__'
        