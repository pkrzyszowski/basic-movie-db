from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle

from .models import Movie, Comment
from .serializers import MovieSerializer, CommentSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    search_fields = ('title', )
    ordering_fields = ('title', 'year')
    throttle_classes = [UserRateThrottle]
    permission_classes = (IsAuthenticated,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('movie',)

    def get_queryset(self):
        if self.kwargs.get('movies__pk', None):
            return self.queryset.filter(movie=self.kwargs['movies__pk'])
        return self.queryset
