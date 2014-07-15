from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from oneanddone.users import models


class MyUserAdmin(UserAdmin):
    def queryset(self, request):
        """
        Only return users if they have signed the privacy policy.
        """
        qs = super(MyUserAdmin, self).queryset(request)
        return qs.filter(profile__privacy_policy_accepted=True)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'privacy_policy_accepted')
    readonly_fields = ('name', 'username')

    def queryset(self, request):
        """
        Only return profiles for users if they have signed the privacy policy.
        """
        qs = super(UserProfileAdmin, self).queryset(request)
        return qs.filter(privacy_policy_accepted=True)


admin.site.register(models.UserProfile, UserProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
