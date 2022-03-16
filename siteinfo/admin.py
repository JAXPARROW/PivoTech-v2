from django.contrib import admin
from siteinfo.models import Cluster, FieldEngineer, FuelStation, Site, FleetVehicle
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from siteinfo.resources import ClusterResource, FieldEngineerResource, FleetVehicleResource, FuelStationResource, SiteResource



class FleetVehicleAdmin(ImportExportModelAdmin):
    resource_class = FleetVehicleResource
    list_display = ['driver_name','plate_number','field_engineer','vehicle_status','phone_number']
    list_editable = ['vehicle_status',]


class FieldEngineerAdmin(ImportExportActionModelAdmin):
    resource_class = FieldEngineerResource
    list_display = ['field_engineer', 'cluster', 'GMT', 'phone_number', 'alternate_number','joining_date','age_of_service',]
    list_editable = ['joining_date','cluster',]


class ClusterAdmin(ImportExportActionModelAdmin):
    resource_class = ClusterResource
    list_display = ['cluster_name','noc_operator','field_supervisor','zonal_manager','zone',]
    list_filter = ['cluster_name','zone', 'zonal_manager',]
    list_search = ['field_engineer',]



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



admin.site.register(FleetVehicle, FleetVehicleAdmin)
admin.site.register(FieldEngineer, FieldEngineerAdmin)
admin.site.register(Cluster, ClusterAdmin)
admin.site.register(FuelStation, FuelStationAdmin)
admin.site.register(Site, SiteAdmin)

admin.site.site_header = "PIVOTECH SITES DATABASE"
admin.site.site_title = "PIVOTECH SITES DATABASE"