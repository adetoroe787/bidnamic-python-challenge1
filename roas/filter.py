from .models import *
import django_filters as Filter
 
class SearchByCampaignFilter(Filter.FilterSet):
    class Meta:
        model = search_terms
        fields = ['structure_value', 'search_term', 'total_cost', 'total_conversion_value']


class SearchByAdgroupFilter(filter.FilterSet):
    class Meta:
        model = search_terms
        fields = ['alias', 'search_term', 'total_cost', 'total_conversion_value']