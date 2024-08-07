from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    flat_name = serializers.CharField()
    prev_booking_id = serializers.IntegerField()

    class Meta:
        model = Booking
        fields = '__all__'