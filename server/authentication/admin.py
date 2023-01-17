from django.contrib import admin
from authentication.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'last_login','first_name','bio','activity_role','company_title', 'password',)
    list_display_links = ('id','email','first_name','company_title')
    search_fields = ('id', 'email','company_title','activity_role',)
    list_editable = ('activity_role',)
    list_filter = ('company_title','activity_role',)

admin.site.register(User, UserAdmin)
