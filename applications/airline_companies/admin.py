from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Point, AviaCompany, Plane, Flight, AviaCompanyImage


class InlineAviaCompanyImage(admin.TabularInline):
    model = AviaCompanyImage
    extra = 1
    fields = ['image', ]


class AviaCompanyAdminDisplay(admin.ModelAdmin):
    inlines = [InlineAviaCompanyImage, ]

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain" />')
        else:
            return ""


admin.site.register(Point)
admin.site.register(Plane)
admin.site.register(AviaCompany, AviaCompanyAdminDisplay)
admin.site.register(Flight)



