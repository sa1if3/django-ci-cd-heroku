from django.contrib import admin
from .models import SampleName


@admin.register(SampleName)
class SampleNameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
