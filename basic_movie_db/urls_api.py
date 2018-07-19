from django.conf.urls import url, include
from rest_framework import routers


from . import views

router = routers.DefaultRouter()

router.register('movies', views.MovieViewSet, base_name='movies')
router.register('comments', views.CommentViewSet, base_name='comments')


urlpatterns = [
    url(r'^', include(router.urls))
]
