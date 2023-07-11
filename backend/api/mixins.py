
## This will handle the permissions in each class views instead of writting it multiple times
from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


#Request user data and customize view querryset using mixin
class UserQuerySetMixin():
    user_field='user'
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        allow_staff_view =False
        lookup_data = {} #This will simply take up all the data stored in the user field
        lookup_data[self.user_field]=self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if allow_staff_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data) #This will return self.user_field=self.request.user. This will narrow down the queryset
