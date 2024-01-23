# yourapp/serializers.py
from rest_framework import serializers
from .models import Ott,Category

class UploadedContentSerializer(serializers.ModelSerializer):
    film_id = serializers.IntegerField(source='id', read_only=True)
    lang_id = serializers.IntegerField(source='category.id', read_only=True)
    genre_id = serializers.IntegerField(source='subcategory.id', read_only=True)

    class Meta:
        model = Ott
        fields = ['film_id', 'title', 'description', 'file', 'uploaded_at', 'status', 'thumbnail', 'lang_id',
                  'genre_id']


# yourapp/serializers.py
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    lang_id = serializers.IntegerField(source='id', read_only=True)  # This line adds a new field 'lang_id' mapped to 'id'

    class Meta:
        model = Category
        fields = ['lang_id', 'name', 'description', 'uploaded_at', 'status']
from .models import Category, Subcategory

class SubcategorySerializer(serializers.ModelSerializer):
    genre_id = serializers.IntegerField(source='id', read_only=True)
    lang_id = serializers.IntegerField(source='category.id', read_only=True)

    class Meta:
        model = Subcategory
        fields = ['genre_id', 'lang_id', 'name', 'description', 'uploaded_at', 'status']


class OttSerializer(serializers.ModelSerializer):
    film_id = serializers.IntegerField(source='id', read_only=True)
    lang_id = serializers.IntegerField(source='category.id', read_only=True)
    genre_id = serializers.IntegerField(source='subcategory.id', read_only=True)

    class Meta:
        model = Ott
        fields = ['film_id', 'title', 'description', 'file', 'uploaded_at', 'status', 'thumbnail', 'lang_id', 'genre_id']
