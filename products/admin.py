from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from unfold.admin import ModelAdmin, TabularInline
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import *

@admin.register(Tag)
class TagAdmin(ModelAdmin):
    pass

class ImageInline(TabularInline):
    model = Image
    extra = 1
    fields = ['image', 'order']
    show_change_link = True

@admin.register(Product)
class ProductAdmin(ModelAdmin, TranslationAdmin):
    @admin.display(description=_("Image"))
    def main_image(self, obj):
        img = obj.images.filter(order=1).first()
        if img:
            return format_html('<img src="{}" width=100 />', img.image.url)
        return '-'
    
    inlines = [ImageInline]
    list_display = ('main_image', 'name', 'price',)

admin.site.register(Image)
