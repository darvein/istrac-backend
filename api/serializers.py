import boto3
from django.conf import settings
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TPlace, Photo, Video, Location, Category, Event, Like, Favorite, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('country', 'city', 'slug', 'latitude', 'longitude')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')

class PhotoSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    original_url = serializers.SerializerMethodField()

    def get_image_url(self, photo):
        request = self.context.get('request')
        if photo.image and hasattr(photo.image, 'url'):
            return request.build_absolute_uri(photo.image.url)
        return None

    def get_original_url(self, photo):
        if photo.image:
            original_key = photo.image.name.replace('photos/', 'p/')
            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            original_url = self.get_presigned_url(bucket_name, original_key)
            return original_url
        return None

    def get_presigned_url(self, bucket_name, object_name, expiration=3600):
        s3_client = boto3.client('s3')
        try:
            response = s3_client.generate_presigned_url('get_object',
                                                        Params={'Bucket': bucket_name,
                                                                'Key': object_name},
                                                        ExpiresIn=expiration)
        except NoCredentialsError:
            print("Credentials not available")
        return response

    class Meta:
        model = Photo
        fields = ('id', 'created_by', 'image', 'image_url', 'original_url')

class VideoSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField()

    def get_video_url(self, video):
        request = self.context.get('request')
        if video.video and hasattr(video.video, 'url'):
            return request.build_absolute_uri(video.video.url)
        return None

    class Meta:
        model = Video
        fields = ('id', 'created_by', 'video', 'video_url')

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    likes = LikeSerializer(many=True, read_only=True)
    favorites = FavoriteSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'created_at', 'likes', 'favorites')

class TPlaceSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    created_by = UserSerializer()
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    favorites = FavoriteSerializer(many=True, read_only=True)

    class Meta:
        model = TPlace
        fields = ('id', 'name', 'slug', 'description', 'location', 'created_by', 
                  'photos', 'videos', 'comments', 'categories', 'likes', 'favorites')

class EventSerializer(serializers.ModelSerializer):
    tplace = TPlaceSerializer()
    created_by = UserSerializer()
    photos = PhotoSerializer(many=True, read_only=True)
    videos = VideoSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    favorites = FavoriteSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'tplace', 'created_by', 'date', 'title', 
                  'photos', 'videos', 'comments', 'likes', 'favorites')
