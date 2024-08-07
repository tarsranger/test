from django.db.models import F, OuterRef, Subquery
from rest_framework import generics, filters
from .models import Booking
from .serializers import BookingSerializer


class BookingListAPI(generics.ListAPIView):
    serializer_class = BookingSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['flat', 'checkin']
    ordering = ['flat', 'checkin']

    def get_queryset(self):
        prev_booking_sub_q = Subquery(
            Booking.objects
            .filter(
                flat=OuterRef('flat'),
                checkin__lt=OuterRef('checkin'),
            )
            .order_by('-checkin')
            .values('id')[:1]
        )

        qs = (
            Booking.objects.all()
            .annotate(
                flat_name=F('flat__name'),
                prev_booking_id=prev_booking_sub_q,
            )
        )

        return qs