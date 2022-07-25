from rest_framework.serializers import ModelSerializer
from base.models import Airline_Companie
from base.views.userSerializion import UserSerializer
from base.views.countrieSerializion import CountrieSerializer

 
class Airline_CompanieSerializer(ModelSerializer):
    class Meta:
        model = Airline_Companie
        fields = '__all__'

    def get_Airline_Companie(self,obj):
        return {
            "id": obj._id,
            "name": str(obj.name),
            "countrie" : CountrieSerializer().get_Countrie(obj.countrie),
            "user": UserSerializer().getUser(obj.user),
            "createdTime": obj.createdTime,     
            }

    def get_All_Airline_Companie(self):
        res=[] #create an empty list
        for AirlineObj in Airline_Companie.objects.all(): #run on every row in the table...
            res.append(self.get_Airline_Companie(AirlineObj)) #append row by to row to res list
        return res


    def get_Airline_Companie_By_Id(self,id):
        countrie= Airline_Companie.objects.get(_id = id)
        return {
            "id": countrie._id,
            "name": str(countrie.name),
            "countrie" : CountrieSerializer().get_Countrie(countrie.countrie),
            "user": UserSerializer().getUser(countrie.user),
            "createdTime": countrie.createdTime,     
            }

