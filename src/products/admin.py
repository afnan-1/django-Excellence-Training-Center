from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
	search_fields=('slug','title','Price')
	list_display = ['__str__','slug','Price',]
admin.site.site_header = "Excellence Training Center"
admin.site.site_title = "Excellence Training Center"
admin.site.index_title = "Welcome to Excellence Training Center"
admin.site.register(Product, ProductAdmin)