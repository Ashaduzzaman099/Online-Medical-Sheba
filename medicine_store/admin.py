from django.contrib import admin
from .models import Medicine, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'power', 'category', 'stock', 'expire_date', 'created_at')
    list_filter = ('category', 'expire_date')
    search_fields = ('name', 'meta_tags')
    readonly_fields = ('created_at', 'updated_at')

