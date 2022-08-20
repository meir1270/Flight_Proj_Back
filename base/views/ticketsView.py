from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.views.customersSerializion import CustomerSerializer
from base.views.flightSerializion import FlightSerializer
from base.views.ticketsSerializion import TicketsSerializer
from base.models import Customer,Tickets,Flight
from base.views.userSerializion import UserSerializer
 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
  
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTickets(request,id=-1):
    if int(id) > -1: #get single product
        return JsonResponse(TicketsSerializer().get_Ticket_By_Id(id),safe=False)
    else: # return all
        return JsonResponse(TicketsSerializer().get_All_Tickets(),safe=False) #return array as json response

 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTickets(request,id=-1):
    temp= Tickets.objects.get(_id = id)
    temp.delete()
    return JsonResponse({'DELETE': id})

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTickets(request):
    print(request.data)
    user = request.user
    Tickets.objects.create(
        customer=Customer.objects.get(_id=request.data['customer_id']),
        flight=Flight.objects.get(_id=request.data['flight_id']),
        number_of_tickets=request.data["number_of_tickets"],
        user=user)
    print(user)
    return JsonResponse({'POST':"success"})
 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTicketsForUSER(request):
    user = request.user
    print(user)
    tickets = user.tickets_set.all()
    return JsonResponse(TicketsSerializer().get_All_Tickets_For_User(tickets),safe=False) #return array as json response
