from rest_framework import serializers
from .models import MovieModel

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        Model = MovieModel
        fields =('id', 'title','description')