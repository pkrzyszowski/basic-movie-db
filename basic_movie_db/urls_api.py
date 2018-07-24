from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from rest_framework_swagger.views import get_swagger_view

from basic_movie_db import views

router = SimpleRouter()

router.register('movies', views.MovieViewSet, base_name='movies')
router.register('comments', views.CommentViewSet, base_name='comments')

movie_router = NestedSimpleRouter(router, r'movies')
movie_router.register(r'comments', views.CommentViewSet, base_name='movie-comments')

schema_view = get_swagger_view(title='Basic DB Movie API')

urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
