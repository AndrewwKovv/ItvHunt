from django.contrib import admin
from candidate.models import Candidate
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id','user_email', 'created_at', 'stage')
    list_display_links = ('id','user_email','stage')
    search_fields = ('id', 'user_email', 'stage')
    # list_editable = ('user_email' ,)
    list_filter = ('stage',)



admin.site.register(Candidate, CandidateAdmin)
