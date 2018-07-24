import json
import requests

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from basic_movie_db.models import Movie


class MovieTest(APITestCase):

    def test_create_movie(self):
        data = {
            'title': 'Rocky'
        }
        url = reverse('api:movies-list')
        response = self.client.post(url, data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_not_found_movie(self):
        data = {
            'title': 'AAbbccddeeff'
        }
        url = reverse('api:movies-list')
        response = self.client.post(url, data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_comment_movie(self):
        movie = Movie.objects.create(title='Casino')
        data = {
            'movie': movie.id,
            'text': 'Komentarz do filmu.'
        }
        url = reverse('api:comments-list')
        response = self.client.post(url, data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_response(self):
        response = requests.get('http://www.omdbapi.com/?t=Rocky&apikey=8a8e17fe')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
