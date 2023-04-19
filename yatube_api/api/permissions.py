from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    Пермишен на безопасный метод запроса, аутентификацию,
    разрешает полный доступ к объекту только автору.
    """

    def has_permission(self, request, view) -> bool:
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj) -> bool:
        return request.method in SAFE_METHODS or obj.author == request.user
