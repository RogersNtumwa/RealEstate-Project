from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'listing', 'user_id', 'name', 'phone', 'email']
    list_filter = ('name',)
    search_fields = ('name', 'listing', 'user_id')
    list_per_page = 25
    list_display_links = ('id', 'name')


admin.site.register(Contact, ContactAdmin)
