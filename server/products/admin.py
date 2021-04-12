from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ("uploaded_by", "title", "description", "price", "created_dt", "updated_ts")
    list_display = ("uploaded_by","title", "description", "price", "created_dt", "updated_ts")
    readonly_fields = ("created_dt", "updated_ts")

    class Meta:
		    model = Product

admin.site.register(Product, ProductAdmin)
