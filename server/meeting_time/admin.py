from django.contrib import admin
from meeting_time.models import MeetingTime
# Register your models here.
class MeeTimeAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'free_time')
    list_display_links = ('id','title',)
    search_fields = ('id', 'title',)
    list_editable = ( 'free_time',)
    list_filter = ('title', 'free_time',)



admin.site.register(MeetingTime, MeeTimeAdmin)