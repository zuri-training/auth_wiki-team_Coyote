from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthLibraryView, CommentAPIView


routers = DefaultRouter()
routers.register('', AuthLibraryView, basename='auth')
app_name = ''


urlpatterns = [
    path("", include(routers.urls)),
    path("<int:pk>/create_comment", CommentAPIView.as_view(), name="create-comment")
]