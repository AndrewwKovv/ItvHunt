from import_export import resources
from vacancy.models import Vacancy

class VacancyResource(resources.ModelResource):
    class Meta:
        model = Vacancy