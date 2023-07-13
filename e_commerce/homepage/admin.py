from django.contrib import admin
from .models import Permission, UserID
# Register your models here.
class AdminPermissions (admin.ModelAdmin):
    list_display = ('id', 'decenttralization')
class AdminUserID(admin.ModelAdmin):
    list_display = ('gmail', 'username','password', 'IDpermission')
admin.site.register(UserID,AdminUserID)
admin.site.register(Permission, AdminPermissions)