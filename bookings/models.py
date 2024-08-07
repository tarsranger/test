from django.db import models
from flats.models import Flat


class Booking(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    checkin = models.DateField(db_index=True)
    checkout = models.DateField()

    class Meta:
        indexes = [
            models.Index('flat', 'checkin', name='flat_checkin_idx')
        ]