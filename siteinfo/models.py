from django.utils import timezone
import datetime

from smart_selects.db_fields import ChainedForeignKey,GroupedForeignKey

from django.db import models
from django.contrib.auth.models import User

# from model_utils import FieldTracker

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
    ("Online","Online"),
    ("Offline","Offline")
)


#currently not used
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



class FuelStation(models.Model):
    station_name = models.CharField(max_length=50 ,blank=False, unique=True, null=True)

    # tracker = FieldTracker()

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

    # tracker = FieldTracker()

    def __str__(self):
        return self.cluster_name


class FE(models.Model):
    username = models.CharField(max_length=30, unique=True)
    cluster = models.ForeignKey('Cluster', null=True, blank=True, on_delete=models.SET_NULL)
    joining_date = models.DateField(blank=True, null=True)
    phone_number = models.IntegerField(unique=True, null=True, blank=True)
    GMT = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username

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
    site_name = models.CharField(max_length=100, blank=False)
    fuel_station = models.ForeignKey('FuelStation', related_name='FuelStation', null=True, on_delete=models.SET_NULL)
    cluster = models.ForeignKey('Cluster', related_name='Cluster', null=True, on_delete=models.SET_NULL)
    region = models.CharField(choices=REGION, max_length=20, null=True)
    # field_engineer = models.ForeignKey('FE', related_name='FieldEngineer', null=True, blank=True, on_delete=models.SET_NULL)
    
    # field_engineer = models.CharField(max_length=50, null=True)
    # field_engineer = GroupedForeignKey(FE, 'cluster',null=True)
    
    field_engineer = ChainedForeignKey(
        Cluster, 
        chained_field='cluster',
        chained_model_field='username',
        show_all=True,
        auto_choose=False,
        null=True
    )

    grid_status = models.CharField(choices=GRID_STATUS, null=True, max_length=10)
    configuration = models.CharField(choices=CONFIGURATION, null=True, max_length=3)
    dg_ownership = models.CharField(choices=DG_OWNERSHIP, null=True, max_length=10)
    site_class = models.CharField(choices=SITE_CLASS, null=True, max_length=10)
    luku_payment = models.CharField(choices=LUKU_PAYMENT, null=True, max_length=20)
    site_status = models.CharField(choices=SITE_STATUS, null=True, max_length=10)
    QSV = models.CharField(choices=YES_NO_SELECTION, null=True, max_length=4, default='NO')
    site_type = models.CharField(choices=SITE_TYPE, null=True, max_length=30)
    criticality = models.CharField(choices=CRITICALITY, null=True, max_length=2)
    dg_present = models.CharField(choices=YES_NO_SELECTION, null=True, max_length=3)
    DG_type = models.CharField(max_length=50, null=True)
    meter_number = models.IntegerField(null=True, blank=True)
    luku_cph = models.DecimalField(max_digits=3, decimal_places=1)
    fuel_cph = models.DecimalField(max_digits=3, decimal_places=1)
    MKII_PLC = models.CharField(choices=YES_NO_SELECTION, max_length=3)
    PLC_locked = models.CharField(choices=YES_NO_SELECTION, max_length=3)
    dg_capacity = models.IntegerField()
    tank_capacity = models.IntegerField(null=True)
    ETA = models.TimeField()
    ERT = models.TimeField()
    
    # tracker = FieldTracker()

    def __str__(self):
        return '{} {}'.format(self.site_name,self.tenant_ID)



