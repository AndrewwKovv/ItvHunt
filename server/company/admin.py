from django.contrib import admin
from company.models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'title', 'created_at', 'image_company')
    list_display_links = ('id','user', 'title',)
    search_fields = ('id','user', 'title',)
    #list_editable = ('title',)
    list_filter = ('title',)

    raw_id_fields = ['vacancies', ]

admin.site.register(Company, CompanyAdmin)
