import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	# end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	#product_name = CharFilter(field_name="product", lookup_expr='contains')
	status_show = CharFilter(field_name="status", lookup_expr='contains')

	class Meta:
		model = Order
		fields = '__all__'
		exclude = ['customer','date_created','status']