from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.
@admin.register(Ministry)
class MinistryAdmin(admin.ModelAdmin):
    fields = ['ministry_name', 'slug']
    search_fields = ['ministry_name']
    prepopulated_fields = {'slug': ('ministry_name',)}


@admin.register(Chapel)
class ChapelAdmin(admin.ModelAdmin):
    fields = ['chapel_name', 'slug']
    search_fields = ['chapel_name']
    prepopulated_fields = {'slug': ('chapel_name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ['service_name', 'slug']
    search_fields = ['service_name']
    prepopulated_fields = {'slug': ('service_name',)}


@admin.register(ChapelHeads)
class ChapelHeadsAdmin(admin.ModelAdmin):
    fields = ['chapel_heads', 'slug']
    search_fields = ['chapel_heads']
    prepopulated_fields = {'slug': ('chapel_heads',)}


@admin.register(Shepherd)
class ShepherdAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'surname']
    search_fields = ['surname', 'phone']
    prepopulated_fields = {'slug': ('surname', 'first_name')}


# @admin.register(Pastor)
# class PastorAdmin(admin.ModelAdmin):
#     list_display = ['title', 'first_name', 'second_name', 'surname']
#     search_fields = ['surname', 'phone_number']
#     prepopulated_fields = {'slug': ('surname',)}


@admin.register(AreaResidence)
class AreaResidenceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('area_residence',)}


@admin.register(Member)
class MemberAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('surname', 'first_name')}
    pass



