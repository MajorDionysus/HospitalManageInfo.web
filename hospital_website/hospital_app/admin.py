from django.contrib import admin
from import_export.admin import ExportMixin
from .models import ListItem, Hyperlink


@admin.register(ListItem)
class ListItemAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'department', 'contact', 'is_visible', 'updated_at')
    list_editable = ('is_visible',)
    search_fields = ('name', 'department')
    ordering = ('-updated_at',)


@admin.register(Hyperlink)
class HyperlinkAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('text', 'url', 'group', 'order', 'updated_at')
    list_editable = ('order',)
    search_fields = ('text', 'group')
    ordering = ('order',)
