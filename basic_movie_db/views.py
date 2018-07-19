from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters

from basic_movie_db.models import Movie, Comment
from basic_movie_db.serializers import MovieSerializer, CommentSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('title', )
    ordering_fields = ('title', 'year')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('movie',)

