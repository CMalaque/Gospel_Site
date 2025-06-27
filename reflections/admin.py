from django.contrib import admin
from .models import SundayInfo, GospelReflection

@admin.register(SundayInfo)
class SundayInfoAdmin(admin.ModelAdmin):
    list_display = ('sunday_title', 'date', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 80px;" />'
        return "(No image)"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image'

@admin.register(GospelReflection)
class GospelReflectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'sunday_info')
