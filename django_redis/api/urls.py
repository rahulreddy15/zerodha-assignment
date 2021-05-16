from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import stock_data

urlpatterns = {
    path('dailyData', stock_data, name="stock_data")
}
urlpatterns = format_suffix_patterns(urlpatterns)
