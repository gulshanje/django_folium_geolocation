from django.apps import AppConfig


class MeasurementAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'measurement_app'
    verbose_name = "Measurement between 2 locations"
