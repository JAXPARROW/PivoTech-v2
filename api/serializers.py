from siteinfo.models import Cluster, FleetVehicle, FuelStation, Site, FieldEngineer
from rest_framework import serializers


from django.contrib.auth.models import User, Group

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email',)


class FleetVehicleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FleetVehicle
        fields = ('driver_name','registration_number','vehicle_status',)
        # fields = '__all__'


class ClusterSerializer(serializers.ModelSerializer):
    # cluster_manager = UserSerializer()
    class Meta:
        model = Cluster
        fields = ('cluster_name','noc_operator','field_supervisor','zonal_manager','zone','maintanance_partner',)


class FieldEngineerSerializer(serializers.ModelSerializer):
    # cluster = ClusterSerializer()
    vehicle = FleetVehicleSerializer()
    class Meta:
        model = FieldEngineer
        # fields = '__all__'
        fields = ('field_engineer','GMT','phone_number', 'joining_date','vehicle',)


class FleetFESerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FieldEngineer
        fields = ('field_engineer','GMT','phone_number', 'joining_date',)


class FuelStationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FuelStation
        fields = ('station_name',)


class SiteSerializer(serializers.ModelSerializer):
    fuel_station = FuelStationSerializer()
    cluster = ClusterSerializer()
    field_engineer = FieldEngineerSerializer()
    # fleet_vehicle = FleetVehicleSerializer()

    class Meta:
        model = Site
        fields = '__all__'
        # fields = ('HTA_ID','site_name', 'site_status','field_engineer','cluster','fuel_station',)

class AllInfoSerializer(serializers.ModelSerializer):
        fuel_station = FuelStationSerializer()
        cluster = ClusterSerializer()
        field_engineer = FieldEngineerSerializer()

        class Meta:
            model = Site
            fields = '__all__'


