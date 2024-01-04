from rest_framework import serializers
from .models import TPlace
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, photo):
        request = self.context.get('request')
        if photo.image and hasattr(photo.image, 'url'):
            return request.build_absolute_uri(photo.image.url)
        return None
                                              
    class Meta:
        model = Photo
        fields = ('id', 'tplace', 'image', 'image_url')
        
class TPlaceSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    class Meta:
        model = TPlace
        fields = ('id', 'name', 'description', 'photos')

