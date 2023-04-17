from posts.models import Comment, Group, Post, Follow
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов модели Post."""

    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ("author", "post")


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов модели Group."""

    class Meta:
        model = Group
        fields = "__all__"


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для объектов модели Follow."""

    class Meta:
        model = Follow
        fields = "__all__"
