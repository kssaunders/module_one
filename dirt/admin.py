from django.contrib import admin
from .models import Beaches, Codes, AllData, References, Finance, Projects, HDC_Beaches, HDC_Data
import dirt.forms
#import dirt.models as models
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from django.contrib.auth.models import User


class BeachesAdmin(admin.ModelAdmin):
    search_fields = ['location']

admin.site.register(Beaches, BeachesAdmin)
admin.site.register(Projects, BeachesAdmin)

# class SLR_BeachesAdmin(admin.ModelAdmin):
#     search_fields = ['location']
#
# admin.site.register(SLR_Beaches, SLR_BeachesAdmin)

class HDC_BeachesAdmin(admin.ModelAdmin):
    search_fields = ['location']

admin.site.register(HDC_Beaches, HDC_BeachesAdmin)


class AllDataAdmin(admin.ModelAdmin):

    raw_id_fields = ("location",)
    # exclude = ['owner']
    list_display=('date', 'location_location', 'item_code', 'quantity','project_project')
    list_filter = ('project__project',('location__city', DropdownFilter),('location__location',DropdownFilter))
    list_editable = ('quantity',)
    def formfield_for_dbfield(self,db_field,request,**kwargs):
        field = super(AllDataAdmin, self).formfield_for_dbfield(db_field, request,**kwargs)
        if db_field.name == 'location':
            field.initial = AllData.objects.latest('date').location.location
        if db_field.name == 'project':
            field.initial = AllData.objects.latest('date').project.project
        if db_field.name == 'length':
            field.initial = AllData.objects.latest('date').length
        if db_field.name == 'date':
            field.initial = AllData.objects.latest('date').date
        return field

    fields = (('date','project','location'),'length','code','quantity', 'owner')
    print(User.username)
    def item_code(self, obj):
        return obj.code.code
    def item_description(self, obj):
        return obj.code.description
    def item_material(self, obj):
        return obj.code.material
    def project_project(self, obj):
        return obj.project.project
    def location_location(self, obj):
        return obj.location.location

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)

admin.site.register(AllData, AllDataAdmin)

class ReferencesAdmin(admin.ModelAdmin):
    list_display = ('subject', 'title', 'abstract', 'author', 'project')
    list_filter = ('subject', 'author')

admin.site.register(References, ReferencesAdmin)
class CodesAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'material', 'source')
    list_filter = ('source', 'material')
admin.site.register(Codes, CodesAdmin)

class FinanceAdmin(admin.ModelAdmin):
    list_display = ('date', 'entry', 'project', 'origin', 'amount')
    list_filter = ('project', 'entry', 'origin')
admin.site.register(Finance, FinanceAdmin)

class  HDC_DataAdmin(admin.ModelAdmin):

    raw_id_fields = ("location",)
    list_display=('date', 'location_location', 'item_code', 'quantity','project_project')
    list_filter = ('project__project',('location__city', DropdownFilter),('location__location',DropdownFilter))
    list_editable = ('quantity',)

    def formfield_for_dbfield(self,db_field,request,**kwargs):
        field = super(HDC_DataAdmin, self).formfield_for_dbfield(db_field, request,**kwargs)
        if db_field.name == 'location':
            field.initial = HDC_Data.objects.latest('date').location.location
        if db_field.name == 'project':
            field.initial = HDC_Data.objects.latest('date').project.project
        if db_field.name == 'length':
            field.initial = HDC_Data.objects.latest('date').length
        if db_field.name == 'date':
            field.initial = HDC_Data.objects.latest('date').date
        return field

    fields = (('date','project','location'),'length','code','quantity')

    def item_code(self, obj):
        return obj.code.code
    def item_description(self, obj):
        return obj.code.description
    def item_material(self, obj):
        return obj.code.material
    def project_project(self, obj):
        return obj.project.project
    def location_location(self, obj):
        return obj.location.location

    def save_model(self, request, obj, form, change):
        object.owner = request.user
        super().save_model(request, obj, form, change)


admin.site.register(HDC_Data, HDC_DataAdmin)



admin.site.site_header = "hammerdirt admin";
admin.site.site_title = "hammerdirt";
