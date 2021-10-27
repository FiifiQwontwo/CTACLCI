from rest_framework import serializers
from .models import *
# from django.contrib.auth.models import User


class MinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministry
        fields = ('id','ministry_name',)


class PastorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastor
        fields = ('id','title', 'first_name', 'second_name', 'surname', 'sex', 'phone_number', 'email_address',)


class ShepherdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shepherd
        fields = ('id','first_name', 'second_name', 'surname', 'sex', 'type',)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id','first_name', 'second_name', 'surname', 'contact_number', 'owner_of_phone_number',
                  'details_of_owner', 'whatsapp_number', 'sex', 'age', 'occupation',
                  'marital_status', 'area_of_residence', 'micro_area_name', 'nearest_landmark', 'phone_usage',
                  'online_service', 'ministries', 'chapel', 'shepherd', 'chapel_head', 'state', 'services',
                  'bacenta_leader',)


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'password')


#
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceMember
        fields = ('id','present_in', 'date', 'member', 'chapel', 'shepherd', 'services',)


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaResidence
        fields = ('id', 'area_residence',
                  )
