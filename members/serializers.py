from .models import *
from rest_framework import serializers

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = '__all__'
    
class ProductSerializers(serializers.ModelSerializer):
    # member = MemberSerializers(many = True, read_only = True)
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1
