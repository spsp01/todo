from django.contrib import admin
from .models import Tasklist
from import_export.admin import ImportExportModelAdmin
from import_export import resources



#admin.site.register(Tasklist)

@admin.register(Tasklist)
class TaskAdmin(ImportExportModelAdmin):
    pass

class BookResource(resources.ModelResource):
    class Meta:
        model = Tasklist


# Register your models here.
