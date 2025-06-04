from django_filters import rest_framework as filters
from apps.filterApp.models import Member

class MemberFilter(filters.FilterSet):
    class Meta:
        model = Member
        fields = ['is_active']
