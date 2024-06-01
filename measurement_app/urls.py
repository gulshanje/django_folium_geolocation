from django.urls import path
from .views import calculateDistanceView

app_name = "measurement_app"

urlpatterns = [
    path('', calculateDistanceView, name='calculatedistanceview'),
]
