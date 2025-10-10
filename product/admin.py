from django.contrib import admin
from product.models import task ,  Typecategory

# Register your models here.
admin.site.register(task)
admin.site.register( Typecategory)