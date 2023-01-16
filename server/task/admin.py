from django.contrib import admin
from task.models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at','update_at','answer', 'title', 'desc', 'language', 'completed')
    fieldsets = (
        ('Создание Задачи', {
            'fields': ('title', 'desc', 'language', 'answer',)
        }),
    )
    list_display_links = ('id','title',)
    search_fields = ('id', 'title','desc','language',)
    list_editable = ('desc', 'language',)
    list_filter = ('update_at', 'title', 'language', 'completed')

    



admin.site.register(Task, TaskAdmin)
