from siteinfo.models import Cluster, FuelStation, Site, FieldEngineer
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



class ClusterSerializer(serializers.ModelSerializer):
    # cluster_manager = UserSerializer()
    class Meta:
        model = Cluster
        fields = ('cluster_name','noc_operator','field_supervisor','zonal_manager','zone','maintanance_partner',)

class FieldEngineerSerializer(serializers.ModelSerializer):
    cluster = ClusterSerializer()
    class Meta:
        model = FieldEngineer
        fields = ('field_engineer','GMT','phone_number', 'joining_date', 'cluster',)
        

class FuelStationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FuelStation
        fields = ('station_name',)


class SiteSerializer(serializers.ModelSerializer):
    fuel_station = FuelStationSerializer()
    cluster = ClusterSerializer()
    # field_engineer = FESerializer()

    class Meta:
        model = Site
        # fields = ('__all__')
        fields = ('HTA_ID','site_name', 'field_engineer', 'site_status','cluster','fuel_station','cluster',)



