from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import datetime
from base.views.airline_CompanieSerializion  import Airline_CompanieSerializer
from base.models import Airline_Companie, Countrie,Flight
from base.views.countrieSerializion import CountrieSerializer
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
 
 
 
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getFlight(request,id=-1):
    user = request.user
    print(user,"innnn")
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
        remaining_tickets=request.data["remaining_tickets"],
        price=request.data["price"],
        user=user)
    print(user)
    return JsonResponse({'POST':"success"})

 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteFlight(request,id=-1):
    user = request.user
    print(user,"innnn")
    temp= Flight.objects.get(_id = id)
    temp.delete()
    return JsonResponse({'DELETE': id})

@api_view(['GET'])
def get_filght_by_filters(request,origin_countrie=-1,destination_countrie=-1,departure_time="",landing_time=""):
    departure_time_obj = datetime.strptime(departure_time, '%Y-%m-%d')
    landing_time_obj = datetime.strptime(landing_time, '%Y-%m-%d')
    res=[]
    selectedFlight = Flight.objects.all()
    if int(origin_countrie) > -1 :
        origin_countrie_id = CountrieSerializer().get_Countrie_By_Id(origin_countrie)["id"]
        selectedFlight = selectedFlight .filter(origin_countrie_id=origin_countrie_id)
    if int(destination_countrie) > -1 :
        destination_countrie_id = CountrieSerializer().get_Countrie_By_Id(destination_countrie)["id"]
        selectedFlight = selectedFlight .filter(destination_countrie_id=destination_countrie_id)
    if departure_time_obj != "" and landing_time_obj != "":
        selectedFlight = selectedFlight.filter(departure_time__range=[departure_time_obj,landing_time_obj])
    selectedFlight = selectedFlight.filter(status = True)
    for flight in selectedFlight:
        res.append(FlightSerializer().get_Flight(flight))
    return JsonResponse(res,safe =False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFlightForAirline(request):
    user = request.user
    flights = user.flight_set.all()
    return JsonResponse(FlightSerializer().get_All_Flights_For_Airline(flights),safe=False) #return array as json response
