from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        
        #to check if request method is safe
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.id == obj.id #returns true if id of current user is same as id of user being accessed/modified