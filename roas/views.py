
from rest_framework import viewsets

from roas.filter import SearchByAdgroupFilter, SearchByCampaignFilter


from .models import *
from .serializers import *
from rest_framework.response import Response


from rest_framework.permissions import IsAuthenticated



class CampaignList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CampaignSerializer
    queryset = campaign.objects.all()




class AdgroupList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = AdgroupSerializer
    queryset = ad_group.objects.all()



class SearchTermList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = search_termsSerializer
    queryset = search_terms.objects.all()


def searchbyCampaign(request):
        search_list = search_terms.objects.all()
        campaign_filter = SearchByCampaignFilter(request.GET, queryset=search_list)
        return Response(request, {'filter': campaign_filter})



def searchbyAdgroup(request):
        search_list = search_terms.objects.all()
        adgroup_filter = SearchByAdgroupFilter(request.GET, queryset=search_list)
        return Response(request, {'filter': adgroup_filter})