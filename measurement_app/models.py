from django.db import models

class Measurement(models.Model):
    location = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    distance  = models.DecimalField(max_digits=12, decimal_places=2)
    createdAt = models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        # return super().__str__()
        return f"Distance from {self.location} to {self.destination} is {self.distance} km/miles"
