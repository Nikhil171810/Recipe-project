from django.contrib import admin
from import_export import resources,fields
from import_export.admin import ImportExportModelAdmin
from .models import*

# Register your models here.
class RecipeResource(resources.ModelResource):
    class Meta:
        model = Recipe
        fields = ('id','recipe_name','recipe_description','recipe_price','recipe_image')
        export_order = ('id','recipe_name','recipe_description','recipe_price','recipe_image')

class RecipeAdmin(ImportExportModelAdmin):
    model = Recipe
    list_display = ['id','recipe_name','recipe_description','recipe_price']
    search_fields = ('id','recipe_name','recipe_description','recipe_price')
    list_display_links = ('id',)

    resource_class = RecipeResource
    readonly_fields = ('recipe_price',)

admin.site.register(Recipe,RecipeAdmin)

#admin.site.register(Recipe)
