from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    Object-level permission to only allow authors of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or obj.author == request.user
        )
