from django.contrib import admin

from .models import Images, Product

class ImagesInline(admin.TabularInline):
    fields = ("image",)
    readonly_fields = ("created_dt", "updated_ts",)
    model = Images
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    fields = ("uploaded_by", "title", "description", "price", "created_dt", "updated_ts")
    list_display = ("uploaded_by","title", "description", "price", "created_dt", "updated_ts")
    readonly_fields = ("created_dt", "updated_ts")

    class Meta:
		    model = Product
    
    inlines = [ImagesInline]

admin.site.register(Product, ProductAdmin)
