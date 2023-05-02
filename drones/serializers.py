from rest_framework import serializers
from .models import *
from .views import *

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    
    drones = serializers.HyperlinkedRelatedField(many = True,
        read_only = True,
        view_name='drone-detail'
    )
    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones'
            
        )
        
class DroneSerializer(serializers.HyperlinkedModelSerializer):
    
    drone_category = serializers.SlugRelatedField(queryset = DroneCategory.objects.all(),slug_field = 'name')
    class Meta:
        model = Drone
        
        fields = (
            'url',
            'name',
            'drone_category',
            'manufecturing_date',
           'has_it_competed',
            'inserted_time'
        )
        
class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    
    drones = DroneSerializer()
    class Meta:
        model = Competition
        fields = (
        'url',
        'pk',
        'distance_in_feet',
        'distance_achievement_date',
        'drone',
        )
            
    
class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
    choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(
    source='get_gender_display',
    read_only=True)
    class Meta:
        model = Pilot
        fields = (
        'url',
        'name',
        'gender',
        'gender_description',
        'race_count',
        'inserted_time',
        'competitions')
        
        
class PilotCompetitionSerializer(serializers.ModelSerializer):
# Display the pilot's name
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')
    # Display the drone's name
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')
    class Meta:
        model = Competition
        fields = (
        'url',
        'pk',
        'distance_in_feet',
        'distance_achievement_date',
        'pilot',
        'drone')