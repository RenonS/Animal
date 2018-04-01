from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from loginsys.models import Profile
# Register your models here.


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(UserAdmin):
    inlines = (ProfileInLine, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
