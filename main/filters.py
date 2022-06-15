from django_filters import rest_framework as filters
from main import models


class BillFilter(filters.FilterSet):

    class Meta:
        model = models.Bill
        fields = ('organization', 'organization__clients' )


class BillsApiFilter(filters.FilterSet):
    organization = filters.CharFilter(method='get_organization')
    client = filters.CharFilter(method='get_client')

    @staticmethod
    def get_organization(queryset, name, value):
        """фильтр по категории"""
        if value:
            queryset = queryset.filter(organization__name=value)

        return queryset

    @staticmethod
    def get_client(queryset, name, value):
        """фильтр по категории"""
        if value:
            queryset = queryset.filter(organization__clients__name=value)

        return queryset
