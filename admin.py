from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, UploadedFile
from .models import StoreInfo


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

@admin.register(StoreInfo)
class StoreInfoAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'store_hours', 'menu_prices')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(UploadedFile)