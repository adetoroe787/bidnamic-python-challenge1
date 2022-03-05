from rest_framework import serializers
from .models import *

class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = campaign
        fields = "__all__"


class AdgroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ad_group
        fields = "__all__"


class search_termsSerializer(serializers.ModelSerializer):

    class Meta:
        model = search_terms
        fields = "__all__"