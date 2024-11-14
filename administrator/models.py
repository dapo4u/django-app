from django.db import models

class Voter(models.Model):
    vin = models.CharField(max_length=17, unique=True)  # Adding VIN field
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add any other relevant fields
