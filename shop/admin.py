from django.contrib import admin
from .models import Category, Product, CartItem, Order,Wallet,AdminWallet
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','category','product_image','price','quantity','description','id')
    fieldsets=((None,{"fields":('product_image','category','product_name','price','quantity','description')}),)
    add_fieldsets=(
        (None,{'classes':("wide",),
               'fields':('product_image','category','product_name','price','quantity','description')},
        )
    )
    search_fields=('product_name',)
    ordering=('product_name',)
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Wallet)
admin.site.register(AdminWallet)