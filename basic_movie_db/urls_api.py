from django.conf.urls import url, include
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from rest_framework_swagger.views import get_swagger_view

from movies.views import MovieViewSet, CommentViewSet

router = SimpleRouter()

router.register('movies', MovieViewSet, base_name='movies')
router.register('comments', CommentViewSet, base_name='comments')

movie_router = NestedSimpleRouter(router, r'movies', lookup='movies')
movie_router.register(r'comments', CommentViewSet, base_name='movie-comments')

schema_view = get_swagger_view(title='Basic DB Movie API')

urlpatterns = [
    url('^$', schema_view),
    url(r'^', include(router.urls)),
]
