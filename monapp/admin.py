from django.contrib import admin
from .models import ImagePost
from .models import CustomUser
# Register your models here.

class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_creation')
    search_fields = ['titre', 'auteur__username']
    actions = ['approve_posts', 'delete_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=True)

    def delete_posts(self, request, queryset):
        queryset.delete()

admin.site.register(ImagePost,ImagePostAdmin)
admin.site.register(CustomUser)

