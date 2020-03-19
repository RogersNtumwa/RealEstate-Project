from django.contrib import admin
from .models import realtor


class realtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_mvp', 'hire_date')
    list_display_links = ('name',)
    list_filter = ('hire_date',)
    list_editable = ('is_mvp',)
    search_fields = ('name', 'is_mvp')


admin.site.register(realtor, realtorAdmin)
