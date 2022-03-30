from import_export import resources, widgets, fields
from import_export.widgets import ForeignKeyWidget

from siteinfo.models import Cluster, FuelStation, Site, FieldEngineer, FleetVehicle



class FleetVehicleResource(resources.ModelResource):

    class Meta:
        model = FleetVehicle
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('registration_number',)
        exclude = ('id',)


class ClusterResource(resources.ModelResource):

    class Meta:
        model = Cluster
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('cluster_name',)
        fields = ('cluster_name','noc_operator','field_supervisor','zonal_manager','zone','maintanance_partner')
        export_order = ('cluster_name','noc_operator','field_supervisor','zonal_manager','zone','maintanance_partner')


class FieldEngineerResource(resources.ModelResource):

    #cluster_item = cluster_name, renamed to avoid circular reference
    cluster_item = fields.Field(
        column_name = 'Clusters',
        attribute = 'cluster',
        widget = ForeignKeyWidget(Cluster, 'cluster_name'),
        saves_null_values = False,
        readonly = False,
    )

    vehicle = fields.Field(
        column_name = 'Vehicle',
        attribute = 'vehicle',
        widget = ForeignKeyWidget(FleetVehicle, 'registration_number'),
        saves_null_values = False,
        readonly = False,
    )

    class Meta:
        model = FieldEngineer
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','cluster')
        import_id_fields = ('field_engineer',)
        fields = ('field_engineer','cluster_item','phone_number','alternate_number','GMT','vehicle','joining_date',)
        export_order = ('field_engineer','cluster_item','phone_number','alternate_number','GMT','vehicle','joining_date',)


class FuelStationResource(resources.ModelResource):

    class Meta:
        model = FuelStation
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('station_name',)
        fields = ('station_name',)
        export_order = ('station_name',)
        

class SiteResource(resources.ModelResource):
    delete = fields.Field(widget=widgets.BooleanWidget())

    def for_delete(self, row, instance):
        return self.fields['delete'].clean(row)

    fuel_station = fields.Field(
        column_name='Fuel Station',
        attribute='fuel_station',
        widget=ForeignKeyWidget(FuelStation, 'station_name'),
        saves_null_values=False,
        readonly=False,
    )

    cluster_item = fields.Field(
        column_name='Clusters',
        attribute='cluster',
        widget=ForeignKeyWidget(Cluster, 'cluster_name'),
        saves_null_values=False,
        readonly=False,
    )

    fe = fields.Field(
        column_name='FE',
        attribute='field_engineer',
        widget=ForeignKeyWidget(FieldEngineer, 'username'),
        saves_null_values=False,
        readonly=False,
    )

    class Meta:
        model = Site 
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('HTA_ID',)

    
        fields = ('HTA_ID','tenant_ID','site_name','fe','fuel_station','cluster__maintanance_partner','grid_status',
                    'configuration','luku_payment' ,'meter_number','fuel_cph','luku_cph','MKII_PLC','PLC_locked', 'QSV',
                        'site_status','DG_type','dg_capacity','tank_capacity','cluster_item','region','dg_present','dg_ownership',
                            'site_class','site_type','criticality','ETA','ERT','htt_class','anchor_tenant','number_of_tenants',
                                'tanesco_region','site_shelter','SPA_Status','site_load','power_type','access_restricted',
                                    'latitude','longitude','restriction_reasons',
                                )
        
        export_order = ('HTA_ID','tenant_ID','site_name','fe','fuel_station','cluster__maintanance_partner','grid_status',
                        'configuration','luku_payment' ,'meter_number','fuel_cph','luku_cph','MKII_PLC','PLC_locked', 'QSV',
                            'site_status','DG_type','dg_capacity','tank_capacity','cluster_item','region','dg_present','dg_ownership',
                                'site_class','site_type','criticality','ETA','ERT','htt_class','anchor_tenant','number_of_tenants',
                                    'tanesco_region','site_shelter','SPA_Status','site_load','power_type','access_restricted',
                                        'latitude','longitude','restriction_reasons',
                                    )




