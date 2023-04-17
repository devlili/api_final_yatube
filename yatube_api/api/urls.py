from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers

app_name = "api"

router_v1 = routers.DefaultRouter()
router_v1.register(r"v1/posts", PostViewSet)
router_v1.register(r"v1/groups", GroupViewSet)
router_v1.register(r"v1/follow", FollowViewSet)
router_v1.register(
    r"v1/posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments"
)

urlpatterns = [
    path("", include(router_v1.urls)),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
]
