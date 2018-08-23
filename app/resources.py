from import_export import resources
from .models import Tasklist

class TaskResource(resources.ModelResource):
    class Meta:
        model = Tasklist