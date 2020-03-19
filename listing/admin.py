from django.contrib import admin
from .models import listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'city', 'price', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'city', 'realtor')
    list_per_page = 5


admin.site.register(listing, ListingAdmin)
