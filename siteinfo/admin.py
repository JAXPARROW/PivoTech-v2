from django.contrib import admin
from siteinfo.models import *
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from siteinfo.resources import ClusterResource, FEResource, FuelStationResource, SiteResource



class FEAdmin(ImportExportActionModelAdmin):
    resource_class = FEResource
    list_display = ['username', 'cluster', 'GMT', 'phone_number', 'joining_date','age_of_service',]
    list_editable = ['joining_date','cluster',]


class ClusterAdmin(ImportExportActionModelAdmin):
    resource_class = ClusterResource
    list_display = ['cluster_name','noc_operator','field_supervisor','zonal_manager','zone',]
    list_filter = ['cluster_name','zone', 'zonal_manager',]
    list_search = ['username',]



class FuelStationAdmin(ImportExportActionModelAdmin):
    resource_class = FuelStationResource
   


# this will clear site database table
def delete_all_Sites(modeladmin, request, queryset):
    queryset = Site.objects.all().delete()
    delete_all_Sites.short_description = "Clear All Entries"

class SiteAdmin(ImportExportModelAdmin):
    resource_class = SiteResource
    actions = [delete_all_Sites]
    list_display = [
        'HTA_ID','tenant_ID','site_name','cluster','field_engineer','fuel_station','fuel_cph','luku_cph','tank_capacity'
    ]
    list_filter = ['cluster','grid_status','configuration','dg_ownership']



admin.site.register(FE, FEAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(FuelStation, FuelStationAdmin)
admin.site.register(Site, SiteAdmin)

admin.site.site_header = "PIVOTECH SITES DATABASE"
admin.site.site_title = "PIVOTECH SITES DATABASE"