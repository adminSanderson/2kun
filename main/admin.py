# main/admin.py
from django.contrib import admin
from .models import Board, Post

admin.site.site_header = 'UpTap Admin'
admin.site.site_title = 'UpTap'
admin.site.index_title = 'Добро пожаловать в админку UpTap'

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'board', 'ip_address', 'created_at')
    list_filter = ('board',)
    readonly_fields = ('ip_address',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.ip_address = request.META.get('REMOTE_ADDR')
        super().save_model(request, obj, form, change)