from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    # check if the request method is allowed, else return
    # whether the author is the origin of the request
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
