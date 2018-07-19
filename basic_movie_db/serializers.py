from rest_framework import serializers
import requests
from rest_framework.exceptions import NotFound

from basic_movie_db.models import Movie, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):
        title = validated_data.get('title')
        url = 'http://www.omdbapi.com/?t={0}&apikey=8a8e17fe'.format(
            title)
        external_data = self.load_movie_data(url)
        if external_data['Response'] == 'True':
            validated_data['actors'] = external_data.get('Actors', None)
            validated_data['year'] = external_data.get('Year', None)
            validated_data['released'] = external_data.get('Released', None)
            validated_data['runtime'] = external_data.get('Runtime', None)
            validated_data['genre'] = external_data.get('Genre', None)
            validated_data['director'] = external_data.get('Director', None)
            validated_data['writer'] = external_data.get('Writer', None)
            validated_data['plot'] = external_data.get('Plot', None)
            validated_data['language'] = external_data.get('Language', None)
        else:
            raise NotFound(external_data)
        return super().create(validated_data)

    @staticmethod
    def load_movie_data(api_url):
        try:
            response = requests.get(api_url, verify=False)
            response.raise_for_status()
            data = response.json()
            return data
        except requests.exceptions.RequestException as err:
            print("Error:", err)
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
