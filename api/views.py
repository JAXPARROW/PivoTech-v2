from api.serializers import AllInfoSerializer, ClusterSerializer, FieldEngineerSerializer, SiteSerializer, FuelStationSerializer, FleetVehicleSerializer
from siteinfo.models import Cluster, Site, FuelStation, FieldEngineer, FleetVehicle

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.throttling import UserRateThrottle
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# from django.contrib.auth.models import User, Group


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class GroupList(generics.ListAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class FleetVehicleList(generics.ListAPIView):
    queryset = FleetVehicle.objects.all()
    serializer_class = FleetVehicleSerializer
    


class ClusterList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('cluster_name', 'noc_operator', 'field_supervisor', 'zonal_manager', 'zone', 'maintanance_partner',)


class SiteList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('HTA_ID','tenant_ID','site_name','field_engineer','fuel_station','cluster__maintanance_partner','grid_status',
                            'configuration', 'luku_payment' , 'meter_number', 'fuel_cph', 'luku_cph', 'MKII_PLC', 'PLC_locked', 'QSV',
                                'site_status', 'DG_type', 'dg_capacity', 'tank_capacity', 'cluster','region','dg_present','dg_ownership',
                                    'site_class', 'site_type', 'criticality', 'ETA', 'ERT',
                            )           


class FuelStationList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = FuelStation.objects.all()
    serializer_class = FuelStationSerializer


class FieldEngineerList(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = FieldEngineer.objects.all()
    serializer_class = FieldEngineerSerializer
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('cluster', 'GMT')

class AllInfoView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Site.objects.all()
    serializer_class = AllInfoSerializer