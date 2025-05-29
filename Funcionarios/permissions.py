from rest_framework import permissions

class IsGestor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.autorizacoes == "G":
            return True
        return False

class IsProfessorReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.autorizacoes == "C":
            return True
        return False
    