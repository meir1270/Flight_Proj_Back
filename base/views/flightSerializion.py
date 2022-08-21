from rest_framework.serializers import ModelSerializer
from base.models import Flight
from base.views.countrieSerializion import CountrieSerializer
from base.views.airline_CompanieSerializion import Airline_CompanieSerializer
 
class FlightSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def get_Flight(self,obj):
        return {
            "id": obj._id,
            "airline_Companie":  Airline_CompanieSerializer().get_Airline_Companie(obj.airline_Companie),
            "origin_countrie":  CountrieSerializer().get_Countrie(obj.origin_countrie),
            "destination_countrie": CountrieSerializer().get_Countrie(obj.destination_countrie),
            "departure_time": obj.departure_time,
            "landing_time": obj.landing_time,
            "remaining_tickets": obj.remaining_tickets,
            "status": obj.status, 
            "price": obj.price, 
            }


    def get_All_Flight(self):
        res=[] #create an empty list
        for flightObj in Flight.objects.all(): #run on every row in the table...
            res.append(self.get_Flight(flightObj)) #append row by to row to res list
        return res


    def get_Flight_By_Id(self,id):
        flight= Flight.objects.get(_id = id)
        return {
            "id": flight._id,
            "airline_Companie":  Airline_CompanieSerializer().get_Airline_Companie(flight.airline_Companie),
            "origin_countrie":  CountrieSerializer().get_Countrie(flight.origin_countrie),
            "destination_countrie": CountrieSerializer().get_Countrie(flight.destination_countrie),
            "departure_time": flight.departure_time,
            "landing_time": flight.landing_time,
            "remaining_tickets": flight.remaining_tickets,
            "status": flight.status,
            "price": flight.price,
            }

    def get_Flights_For_Airline(self,obj):
        return {
            "id": obj._id,
            "airline_Companie":  Airline_CompanieSerializer().get_Airline_Companie(obj.airline_Companie),
            "origin_countrie":  CountrieSerializer().get_Countrie(obj.origin_countrie),
            "destination_countrie": CountrieSerializer().get_Countrie(obj.destination_countrie),
            "departure_time": obj.departure_time,
            "landing_time": obj.landing_time,
            "remaining_tickets": obj.remaining_tickets,
            "status": obj.status, 
            "price": obj.price, 
            }   

    def get_All_Flights_For_Airline(self,flights):
        res=[] #create an empty list
        for flightObj in flights: #run on every row in the table...
            res.append(self.get_Flights_For_Airline(flightObj)) #append row by to row to res list
        return res




