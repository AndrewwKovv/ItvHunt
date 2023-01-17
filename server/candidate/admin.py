from django.contrib import admin
from candidate.models import Candidate
# Register your models here.
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id','email_candidate', 'created_at', 'stage')
    list_display_links = ('id','email_candidate')
    search_fields = ('id','email_candidate', 'stage')
    list_editable = ('stage' ,)
    list_filter = ('stage',)



admin.site.register(Candidate, CandidateAdmin)
