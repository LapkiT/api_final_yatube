from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet
)

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path(
        'jwt/create/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'jwt/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'jwt/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
]
