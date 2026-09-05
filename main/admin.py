
from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product, Enquiry


# =========================================================
# CATEGORY ADMIN
# =========================================================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'image_preview',
    )

    search_fields = (
        'name',
    )

    class Media:
        css = {
            'all': ('admin/admin.css',)
        }

    def image_preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" '
                'style="width:60px; height:60px; '
                'object-fit:contain; border-radius:6px; '
                'background:#f1f2f3; padding:4px;">',
                obj.image.url
            )

        return "No Image"

    image_preview.short_description = "Image"


# =========================================================
# PRODUCT ADMIN
# =========================================================

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'image_preview',
        'name',
        'category',
        'product_type',
        'price',
        'available',
    )

    search_fields = (
        'name',
        'product_type',
        'description',
        'specifications',
    )

    list_filter = (
        'category',
        'available',
    )

    list_editable = (
        'available',
    )

    fieldsets = (

        (
            'PRODUCT INFORMATION',
            {
                'fields': (
                    'category',
                    'name',
                    'product_type',
                )
            }
        ),

        (
            'PRODUCT DESCRIPTION',
            {
                'fields': (
                    'description',
                    'specifications',
                )
            }
        ),

        (
            'PRICING & AVAILABILITY',
            {
                'fields': (
                    'price',
                    'available',
                )
            }
        ),

        (
            'PRODUCT IMAGE',
            {
                'fields': (
                    'image',
                    'image_preview_admin',
                )
            }
        ),

    )

    readonly_fields = (
        'image_preview_admin',
    )

    class Media:
        css = {
            'all': ('admin/admin.css',)
        }

    # -----------------------------------------------------
    # PRODUCT LIST IMAGE
    # -----------------------------------------------------

    def image_preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" '
                'style="width:70px; height:70px; '
                'object-fit:contain; '
                'border-radius:8px; '
                'border:1px solid #d2d5d7; '
                'background:#f5f6f7; '
                'padding:5px;">',
                obj.image.url
            )

        return "No Image"

    image_preview.short_description = "Image"

    # -----------------------------------------------------
    # PRODUCT IMAGE IN EDIT PAGE
    # -----------------------------------------------------

    def image_preview_admin(self, obj):

        if obj and obj.image:

            return format_html(
                '<div style="padding:15px; '
                'background:#f1f2f3; '
                'border:1px solid #d2d5d7; '
                'border-radius:8px; '
                'display:inline-block;">'
                '<img src="{}" '
                'style="max-width:300px; '
                'max-height:300px; '
                'object-fit:contain; '
                'display:block;">'
                '</div>',
                obj.image.url
            )

        return format_html(
            '<span style="color:#777;">{}</span>',
            'No image uploaded'
        )

    image_preview_admin.short_description = "Current Image"


# =========================================================
# ENQUIRY ADMIN
# =========================================================

@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'company',
        'phone',
        'email',
        'location',
        'products_list',
        'created_at',
    )

    search_fields = (
        'name',
        'company',
        'phone',
        'email',
        'location',
        'message',
        'products__name',
    )

    list_filter = (
        'created_at',
        'products',
    )

    filter_horizontal = (
        'products',
    )

    readonly_fields = (
        'created_at',
    )

    class Media:
        css = {
            'all': ('admin/admin.css',)
        }

    # -----------------------------------------------------
    # SELECTED PRODUCTS
    # -----------------------------------------------------

    def products_list(self, obj):

        products = obj.products.all()

        if products:

            return ", ".join(
                product.name
                for product in products
            )

        return "No product selected"

    products_list.short_description = "Products"



