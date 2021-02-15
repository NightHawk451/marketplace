from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ("title", "description", "price", "created_dt", "updated_ts")
    list_display = ("title", "description", "price", "created_dt", "updated_ts")
    readonly_fields = ("created_dt", "updated_ts")

    class Meta:
		    model = Product

admin.site.register(Product, ProductAdmin)
