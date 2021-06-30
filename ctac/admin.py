from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class MinistryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('ministry_name',)}


class ChapelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('chapel_name',)}


class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('service_name',)}


class ChapelHeadsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('chapel_heads',)}


class ShepherdAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('surname', 'first_name')}


class PastorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('surname',)}


class AreaResidenceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('area_residence',)}


class MemberAdmin(admin.ModelAdmin, ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('surname', 'first_name')}


admin.site.register(Member, MemberAdmin)
admin.site.register(Ministry, MinistryAdmin)
admin.site.register(Chapel, ChapelAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ChapelHeads, ChapelHeadsAdmin)
admin.site.register(Pastor, PastorAdmin)
admin.site.register(Shepherd, ShepherdAdmin)
admin.site.register(AreaResidence, AreaResidenceAdmin)
admin.site.register(AttendanceMember)
admin.site.register(Names)
