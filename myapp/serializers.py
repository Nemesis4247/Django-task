from .models import Banks, Branches
from rest_framework import serializers


class BankSerializer(serializers.ModelSerializer):
    class Meta():
        model = Banks
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    class Meta():
        model = Branches
        fields = ['bank', 'ifsc', 'branch', 'address', 'city', 'district', 'state']
