from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        
        #to check if request method is safe
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id #returns true if id of current user is same as id of user being accessed/modified

class UpdateOwnFeed(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.user_profile.id == request.user.id
