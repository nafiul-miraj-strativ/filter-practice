from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from apps.filterApp.models import Member
from .serializers import MemberSerializer
from .filters import MemberFilter

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class= MemberSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_class = MemberFilter