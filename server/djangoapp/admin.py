from django.contrib import admin
from .models import CarMake, CarModel

admin.site.register(CarModel)

class CarModelInline(admin.TabularInline):
    model = CarModel
    fields = ['name', 'type', 'year', 'dealerid']
    can_delete = False
    show_change_link = True
    extra = 0

@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
   inlines = [CarModelInline,]
   extra = 0

# @admin.register(CarMake)
# class CarMakeAdmin(admin.ModelAdmin):
#     inlines = [CarModelInline]
# admin.site.register(CarModel,CarMakeAdmin)
# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
