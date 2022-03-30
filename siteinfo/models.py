from django.utils import timezone
import datetime

from smart_selects.db_fields import ChainedForeignKey,GroupedForeignKey

from django.db import models
from django.contrib.auth.models import User


CONFIGURATION =( 
    ('GHS','GHS'),
    ('GHX','GHX'),
    ('GXX','GXX'),
    ('OHS','OHS'),
    ('OHX','OHX'),
    ('OXX','OXX')
)

DG_OWNERSHIP = (
   ( "HTT-DG","HTT-DG"),
   ("LL-DG","LL-DG"),
   ("NON-DG","NON-DG")
)

ZONE = (
    ("Coastal","Coastal"),
    ("Northern","Northern"),
    ("Southern","Southern")
)

REGION = (
    ("Dar es salaam","Dar es salaam"),
    ("Tanga","Tanga"),
    ("Pwani","Pwani"),
    ("Lindi","Lindi"),
    ("Mtwara","Mtwara"),
    ("Ruvuma","Ruvuma"),
    ("Morogoro","Morogoro")
)

GRID_STATUS = (
    ("Off Grid","Off Grid"),
    ("Grid","Grid")
)

SITE_CLASS = (
    ("Platinum","Platinum"),
    ("Gold","Gold"),
    ("Silver","Silver")
)

LUKU_PAYMENT =( 
    ("Post-Paid", "Post-Paid"),
    ("Pre-Paid","Pre-Paid"),
    ("Off-Grid","Off-Grid"),
    ("LandLord","LandLord"),
    ("Consolidated","Consolidated")
)

SITE_STATUS =(
    ("On Air","On Air"),
    ("Decomisioned","Decomisioned")
)

VISIT_TYPE =(
    ("QSV","QSV"),
    ("1SVM","1SVM")
)

SITE_TYPE = (
    ("IBS","IBS"),
    ("Roof Top","Roof Top"),
    ("Green Field","Green Field")
)

CRITICALITY =( 
    ("C1","C1"),
    ("C2","C2")
)

#this will be used in any dropdown where selection is yes or no
YES_NO_SELECTION = (
    ("YES","YES"),
    ("NO","NO"),
)

#Issues hindering access restriction to the sites
ACCESS_RESTRICTION = (
    ("Safety Reasons","Safety Reasons"),
    ("Permit Reasons", "Permit Reasons"),
    ("No Restriction", "No Restriction"),
)

VEHICLE_STATUS = (
    ("In Service","In Service"),
    ("Out of Service","Out of Service"),
)

SPA_SELECTION = (
    ('Configured', 'Configured'),
    ('Non-Configured', 'Non-Configgured'),
    ('Optimized', 'Optimized'),
)

SITE_SHELTER = (
    ('Indoor', 'Indoor'),
    ('Outdoor', 'Outdoor'),
)

HTT_CLASS = (
    ('B','B'),
    ('C','C'),
)

CAR_OWNERSHIP = (
    ('Leased', 'Leased'),
    ('Owned', 'Owned'),
)

POWER_TYPE = (
    ('AC','AC'),
    ('DC','DC')
)

class FleetVehicle(models.Model):
    driver_name = models.CharField(max_length=50, blank=False, unique=True, null=True)
    registration_number = models.CharField(max_length=10, blank=False, unique=True, null=True)
    phone_number = models.IntegerField(blank=False, unique=True, null=True)
    vehicle_status = models.CharField(choices=VEHICLE_STATUS, max_length=50, blank=True, null=True, default="In Service")
    car_ownership = models.CharField(choices=CAR_OWNERSHIP, max_length=50, blank=True, default='Owned')

    class Meta:
        verbose_name = 'Fleet Vehicle'
        verbose_name_plural = 'Fleet Vehicles'

    def __str__(self):
        return self.registration_number



class FuelStation(models.Model):
    station_name = models.CharField(max_length=50 ,blank=False, unique=True, null=True)
    class Meta:
        verbose_name = 'Fuel Station'
        verbose_name_plural = 'Fuel Stations'
        
    def __str__(self):
        return self.station_name


class Cluster(models.Model):
    cluster_name = models.CharField(max_length=50,unique=True,blank=False, null=True)
    noc_operator = models.CharField(max_length=100, blank=False)
    field_supervisor = models.CharField(max_length=100, blank=False)
    zonal_manager = models.CharField(max_length=100, blank=False)
    zone = models.CharField(choices=ZONE, max_length=20, blank=False)
    maintanance_partner = models.CharField(max_length=15, blank=False, default='PIVOTECH')

    def __str__(self):
        return self.cluster_name



class FieldEngineer(models.Model):
    cluster = models.ForeignKey('Cluster', null=True, blank=True, on_delete=models.SET_NULL)
    field_engineer = models.CharField(max_length=30, unique=True)
    joining_date = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(unique=True, null=True, blank=True)
    alternate_number = models.IntegerField(unique=True, null=True, blank=True)
    GMT = models.CharField(max_length=20, null=True, blank=True)
    vehicle = models.OneToOneField(FleetVehicle, on_delete=models.SET_NULL, null=True, primary_key=False)

    def __str__(self):
        return self.field_engineer
    class Meta:
        verbose_name = 'Field Engineer'
        verbose_name_plural = 'Field Engineers'

    @property
    def age_of_service(self):
        age_of_service = (datetime.datetime.now().date() - self.joining_date).days
        return age_of_service
        


class Site(models.Model):
    HTA_ID = models.CharField(primary_key=True, max_length=10, unique=True, blank=False)
    tenant_ID = models.CharField(max_length=10, blank=False)
    site_name = models.CharField(max_length=100, blank=False, null=True)
    anchor_tenant = models.CharField(max_length=30, blank=False, null=True)
    number_of_tenants = models.IntegerField(null=True, blank=True)
    fuel_station = models.ForeignKey('FuelStation', related_name='FuelStation', null=True, on_delete=models.SET_NULL)
    cluster = models.ForeignKey('Cluster', related_name='Cluster', null=True, on_delete=models.SET_NULL)
    region = models.CharField(choices=REGION, max_length=50, null=True)    
    field_engineer = ChainedForeignKey(
        FieldEngineer, 
        chained_field='cluster',
        chained_model_field='cluster',
        show_all=False,
        auto_choose=False,
        sort=True)
    grid_status = models.CharField(choices=GRID_STATUS, default='Grid', null=True, max_length=50)
    configuration = models.CharField(choices=CONFIGURATION, default='GXX', null=True, max_length=50)
    dg_ownership = models.CharField(choices=DG_OWNERSHIP, default='HTT-DG', null=True, max_length=50)
    site_class = models.CharField(choices=SITE_CLASS, default='Silver', null=True, max_length=50)
    luku_payment = models.CharField(choices=LUKU_PAYMENT, default='Pre-Paid', null=True, max_length=50)
    site_status = models.CharField(choices=SITE_STATUS, default='Online', null=True, max_length=50)
    htt_class = models.CharField(choices=HTT_CLASS, default='C',null=True, max_length=10)
    QSV = models.CharField(choices=YES_NO_SELECTION, null=True, max_length=50, default='NO')
    site_type = models.CharField(choices=SITE_TYPE, default='Green Field', null=True, max_length=250)
    criticality = models.CharField(choices=CRITICALITY, default='C1', null=True, max_length=50)
    dg_present = models.CharField(choices=YES_NO_SELECTION, default='YES', null=True, max_length=50)
    DG_type = models.CharField(max_length=250, null=True)
    tanesco_region = models.CharField(max_length=250, null=True, blank=True)
    meter_number = models.IntegerField(null=True, blank=True)
    luku_cph = models.DecimalField(max_digits=10, decimal_places=1)
    fuel_cph = models.DecimalField(max_digits=10, decimal_places=1)
    SPA_Status = models.CharField(choices=SPA_SELECTION, max_length=50, default='Optimized', null=True, blank=True)
    site_load = models.CharField(max_length=10, null=True, blank=True)
    power_type = models.CharField(choices=POWER_TYPE, max_length=50, default='DC', null=True, blank=True)
    MKII_PLC = models.CharField(choices=YES_NO_SELECTION, default='YES', max_length=50)
    PLC_locked = models.CharField(choices=YES_NO_SELECTION, default='YES', max_length=50)
    dg_capacity = models.IntegerField()
    tank_capacity = models.IntegerField(null=True)
    site_shelter = models.CharField(choices=SITE_SHELTER, default='Outdoor',max_length=50, null=True, blank=True)
    ETA = models.TimeField()
    ERT = models.TimeField()
    access_restricted = models.CharField(choices=YES_NO_SELECTION, default='NO',max_length=50, null=True, blank=True)
    restriction_reasons = models.CharField(choices=ACCESS_RESTRICTION, default="No Restriction",max_length=250, null=True, blank=True)
    latitude   = models.FloatField(blank=True, null=True)
    longitude   = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return '{} {}'.format(self.site_name,self.tenant_ID)

