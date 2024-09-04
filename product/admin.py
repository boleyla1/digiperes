from django.contrib import admin
from . import models


class InformationAdmin(admin.StackedInline):
    model = models.Information


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    inlines = [InformationAdmin]


# @admin.register(models.Image)
# class ImageAdmin(admin.ModelAdmin):
#     multiupload_form = True
#     multiupload_list = True


# admin.site.register(models.Product)
admin.site.register(models.Size)
admin.site.register(models.Color)
# admin.site.register(models.Image)
admin.site.register(models.Brand)
admin.site.register(models.Category)
# Register your models here.
