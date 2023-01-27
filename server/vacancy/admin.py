from django.contrib import admin
from vacancy.models import Vacancy
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class VacancyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'created_at', 'title', 'link_vacancy')
    list_display_links = ('id','title','link_vacancy')
    search_fields = ('id', 'title','link_vacancy')
    #list_editable = ('link_vacancy')
    list_filter = ('link_vacancy','title',)

    raw_id_fields = ['candidate', ]



admin.site.register(Vacancy, VacancyAdmin)
