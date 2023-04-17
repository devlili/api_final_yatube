from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет для объектов модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для объектов модели Group."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для объектов модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет для объектов модели Follow."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
