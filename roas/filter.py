from .models import *
import django_filters as Filter
 
class SearchByCampaignFilter(Filter.FilterSet):
    class Meta:
        model = search_terms
        fields = ['campaign', 'search_term', 'cost', 'conversion_value','roas']


class SearchByAdgroupFilter(Filter.FilterSet):
    class Meta:
        model = search_terms
        fields = ['ad_group', 'search_term', 'cost', 'conversion_value','roas']