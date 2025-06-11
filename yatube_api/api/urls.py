from django.urls import include, path
from .views import (PostViewSet, GroupViewSet, CommentViewSet,
                    FollowList)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('v1/posts', PostViewSet)
router.register('v1/groups', GroupViewSet)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/follow/', FollowList.as_view()),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]