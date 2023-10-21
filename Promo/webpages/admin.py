from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    
    def display_picture(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))
    
    list_display = ('id', 'display_picture', 'first_name', 'channel_name', 'role', 'created_date')
    list_display_links = ('first_name', 'id')
    search_field = ('first_name', 'role')
    list_filter = ('role',)


admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)