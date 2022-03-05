import csv
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *

from .filter import *


fs = FileSystemStorage(location='tmp/')


# Campaign Serializer
class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = campaign
        fields = "__all__"


# Campaign Viewset to upload csv file to model
class CampaignViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Campaign.
    """
    queryset = campaign.objects.all()
    serializer_class = CampaignSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]

        content = file.read()  # these are bytes
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        
        campaign_list = []
        for id_, row in enumerate(reader):
            (
                campaign_id,
                structure_value,
                status,
            ) = row
            campaign_list.append(
                campaign(
                    campaign_id = campaign_id,
                    structure_value = structure_value,
                    status = status
                )
            )

        campaign.objects.bulk_create(campaign_list)

        return Response("Successfully upload the data")


# adgroup Serializer
class AdgroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = adgroups
        fields = "__all__"


# adgroup Viewset to upload csv file to model
class AdgroupViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Campaign.
    """
    queryset = adgroups.objects.all()
    serializer_class = AdgroupSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]

        content = file.read()  # these are bytes
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        
        adgroup_list = []
        for id_, row in enumerate(reader):
            (
                ad_group_id,
                campaign,
                alias,
                status,
            ) = row
            adgroup_list.append(
                adgroups(
                    ad_groud_id =ad_group_id,
                    campaign_id = campaign,
                    alias = alias,
                    status = status,
                )
            )

        adgroups.objects.bulk_create(adgroup_list)

        return Response("Successfully upload the data")


# adgroup Serializer
class search_termsSerializer(serializers.ModelSerializer):

    class Meta:
        model = search_terms
        fields = "__all__"


# adgroup Viewset to upload csv file to model
class search_termsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Campaign.
    """
    queryset = search_terms.objects.all()
    serializer_class = search_termsSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        """Upload data from CSV"""
        file = request.FILES["file"]

        content = file.read()  # these are bytes
        file_content = ContentFile(content)
        file_name = fs.save(
            "_tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        
        search_terms_list = []
        for id_, row in enumerate(reader):
            (
                date,
                ad_group,
                campaign,
                clicks,
                cost,
                conversion_value,
                conversions,
                search_term
            ) = row
            search_terms_list.append(
                search_terms(
                    date = date,
                    ad_group_id = ad_group,
                    campaign_id = campaign,
                    clicks = clicks,
                    cost = cost,
                    conversion_value =conversion_value ,
                    conversions =conversions  ,
                    search_term = search_term ,
                )
            )

        search_terms.objects.bulk_create(search_terms_list)

        return Response("Successfully upload the data")

