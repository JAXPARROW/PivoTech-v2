from import_export import resources, widgets, fields
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

from siteinfo.models import *



class ClusterResource(resources.ModelResource):

    class Meta:
        model = Cluster
        skip_unchanged = True
        report_skipped = True
        # exclude = ('id',)
        # import_id_fields = ('cluster_name')



class FEResource(resources.ModelResource):

    #cluster_item = cluster_name, renamed to avoid circular reference
    cluster_item = fields.Field(
        column_name='Clusters',
        attribute='cluster',
        widget=ForeignKeyWidget(Cluster, 'cluster_name'),
        saves_null_values=False,
        readonly=False,
    )

    class Meta:
        model = FE
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','cluster')
        import_id_fields = ('username',)
        fields = ('username', 'cluster_item','phone_number','GMT', 'joining_date',)
        export_order = ('username', 'cluster_item','phone_number','GMT', 'joining_date',)



class FuelStationResource(resources.ModelResource):

    class Meta:
        model = FuelStation
        skip_unchanged = True
        report_skipped = True
        # exclude = ('id',)
        # import_id_fields = ('station_name')
        

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
        widget=ForeignKeyWidget(FE, 'username'),
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
                    'configuration', 'luku_payment' , 'meter_number', 'fuel_cph', 'luku_cph', 'MKII_PLC', 'PLC_locked', 'QSV',
                        'site_status', 'DG_type', 'dg_capacity', 'tank_capacity', 'cluster_item','region','dg_present','dg_ownership',
                            'site_class', 'site_type', 'criticality', 'ETA', 'ERT', 
                                )
        
        export_order = ('HTA_ID','tenant_ID','site_name','fe','fuel_station','cluster__maintanance_partner','grid_status',
                            'configuration', 'luku_payment' , 'meter_number', 'fuel_cph', 'luku_cph', 'MKII_PLC', 'PLC_locked', 'QSV',
                                'site_status', 'DG_type', 'dg_capacity', 'tank_capacity','cluster_item','region','dg_present', 'dg_ownership',
                                    'site_class', 'site_type', 'criticality', 'ETA', 'ERT', 
                                        )
