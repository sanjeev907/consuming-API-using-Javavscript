from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, error_messages={'name':"name is required"})
    age = serializers.IntegerField(required=True,error_messages={'age':'age is required'})
    test = serializers.CharField(required=True,error_messages={'test':'age is required'})
    B2B_price = serializers.IntegerField(required=True,error_messages={'B2B_price':'price is required'})
    status = serializers.CharField(required=True,error_messages={'status':'status is required'})
    B2C_price = serializers.IntegerField(required=True,error_messages={'B2B_price':'price is required'})
    B2C_Status = serializers.CharField(required=True,error_messages={'status':'status is required'})
    # date = serializers.DateTimeField()