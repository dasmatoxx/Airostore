from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import TicketBook, TypeClass, Flight
from .serializers import TicketBookSerializer, TypeClassSerializer, TicketSerializer


class TypeClassView(ListAPIView):
    queryset = TypeClass.objects.all()
    serializer_class = TypeClassSerializer


class TicketView(ListAPIView):
    queryset = TicketBook.objects.all()
    serializer_class = TicketSerializer


class TicketCreateView(generics.CreateAPIView):
    queryset = TicketBook.objects.all()
    serializer_class = TicketBookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = TicketBookSerializer(data=request.data)
        if serializer.is_valid():
            seat = request.data['seat']
            flight = Flight.objects.get(id=request.data['flight'])
            if TicketBook.objects.filter(flight=flight, seat=seat, status__exact='accepted').exists():
                return Response({"message: the seat is busy"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save(user=self.request.user)
                ticket = TicketBook.objects.filter(flight=flight, seat=seat, status__exact='pending').order_by('-id').first()
                ticket.total_price = ticket.type.price + flight.price
                ticket.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




