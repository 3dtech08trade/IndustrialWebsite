from django.contrib import admin
from .models import Category, Product, Enquiry

admin.site.register(Category)
admin.site.register(Product)

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'company',
        'phone',
        'email',
        'location',
        'created_at'
    )

    search_fields = (
        'name',
        'company',
        'phone',
        'email'
    )

    list_filter = (
        'created_at',
    )