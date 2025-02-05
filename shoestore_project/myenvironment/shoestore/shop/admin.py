from django.contrib import admin
from .models import Category, Product, Variation

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug']
	prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','price','stock','available','created','updated']
	list_editable = ['price','stock','available']
	prepopulated_fields = {'slug':('name',)}
	list_per_page = 20

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Variation, VariationAdmin)