from django.contrib import admin

# Register your models here.
from .models import car

# to view as entites


class AdminDescr(admin.ModelAdmin):
    list_display = ['name', 'gender', 'image']
    list_editable = ['gender']
    search_fields = ['name']
    list_filter = ['gender']


admin.site.register(car, AdminDescr)
