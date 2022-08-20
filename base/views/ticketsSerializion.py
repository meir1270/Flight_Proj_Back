from rest_framework.serializers import ModelSerializer
from base.models import Tickets
from base.views.customersSerializion import CustomerSerializer
from base.views.flightSerializion import FlightSerializer
 
class TicketsSerializer(ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'

    def get_Tickets(self,obj):
        return {
            "id": obj._id,
            "flight":  FlightSerializer().get_Flight(obj.flight),
            "customer": CustomerSerializer().get_Customer(obj.customer),
            "number_of_tickets" : obj.number_of_tickets
 }

    def get_All_Tickets(self):
        res=[] #create an empty list
        for ticketsObj in Tickets.objects.all(): #run on every row in the table...
            res.append(self.get_Tickets(ticketsObj)) #append row by to row to res list
        return res


    def get_Ticket_By_Id(self,id):
        tickets= Tickets.objects.get(_id = id)
        return {
            "id": tickets._id,
            "flight": FlightSerializer().get_Flight(tickets.flight),
            "customer": CustomerSerializer().get_Customer(tickets.customer),
            "number_of_tickets" : tickets.number_of_tickets
            }  

    def get_Tickets_By_User(self,obj):
        # tickets = user.tickets_set.all()
        return {
            "id": obj._id,
            "flight":  FlightSerializer().get_Flight(obj.flight),
            "customer": CustomerSerializer().get_Customer(obj.customer),
            "number_of_tickets" : obj.number_of_tickets
            }


    def get_All_Tickets_For_User(self,tickets):
        res=[] #create an empty list
        for ticketsObj in tickets: #run on every row in the table...
            res.append(self.get_Tickets_By_User(ticketsObj)) #append row by to row to res list
        return res

