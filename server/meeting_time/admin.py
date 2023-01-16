from django.contrib import admin
from meeting_time.models import MeetingTime
# Register your models here.
class MeeTimeAdmin(admin.ModelAdmin):
    list_display = ('id','title','close_time', 'free_time')
    list_display_links = ('id','title',)
    search_fields = ('id', 'title',)
    list_editable = ('close_time', 'free_time',)
    list_filter = ('title', 'close_time',)



admin.site.register(MeetingTime, MeeTimeAdmin)