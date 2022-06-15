from rest_framework import serializers
from main import models


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Organization
        fields = ('name', )

class BillsSerializer(serializers.ModelSerializer):

    organization = serializers.SerializerMethodField()

    class Meta:
        model = models.Bill
        fields = ('id', 'number', 'sum_bill', 'organization')

    @staticmethod
    def get_organization(obj):
        return OrganizationSerializer(obj.organization).data
