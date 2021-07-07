from django.contrib import admin
from projects.models import Project

# Register your models here.
class ProjectField(admin.ModelAdmin):
    list_display = ('title', 'description', 'technology', 'image')
admin.site.register(Project,ProjectField)