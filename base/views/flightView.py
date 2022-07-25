from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 
from base.views.airline_CompanieSerializion  import Airline_CompanieSerializer
from base.models import Airline_Companie, Countrie,Flight
from base.views.flightSerializion import FlightSerializer
 
 
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
 
 
 
@api_view(['GET','DELETE'])
# @permission_classes([IsAuthenticated])
def getFlight(request,id=-1):
    user = request.user
    print(user,"innnn")
    if request.method == 'DELETE': #method delete a row
        temp= Flight.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if int(id) > -1: #get single product
        return JsonResponse(FlightSerializer().get_Flight_By_Id(id),safe=False)
    else: # return all
        return JsonResponse(FlightSerializer().get_All_Flight(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addFlight(request):
    print(request.data)
    user = request.user
    Flight.objects.create(
        airline_Companie=Airline_Companie.objects.get(_id=request.data['airline_Companie_id']),
        origin_countrie=Countrie.objects.get(_id=request.data['origin_countrie_id']),
        destination_countrie=Countrie.objects.get(_id=request.data['destination_countrie_id']),
        departure_time=request.data["departure_time"],
        landing_time=request.data["landing_time"],
        remaining_tickets=request.data["remaining_tickets"],)
    print(user)
    return JsonResponse({'POST':"success"})

