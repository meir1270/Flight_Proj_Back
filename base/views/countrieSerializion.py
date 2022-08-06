from rest_framework.serializers import ModelSerializer
from base.models import Countrie
 
 
class CountrieSerializer(ModelSerializer):
    class Meta:
        model = Countrie
        fields = '__all__'

    def get_Countrie(self,obj):
        return {
            "id": obj._id,
            "name": str(obj.name),
            "image": str(obj.image),
            }

    def get_All_Countrie(self):
        res=[] #create an empty list
        for countrieObj in Countrie.objects.all(): #run on every row in the table...
            res.append(self.get_Countrie(countrieObj)) #append row by to row to res list
        return res


    def get_Countrie_By_Id(self,id):
        countrie= Countrie.objects.get(_id = id)
        return {
            "id": countrie._id,
            "name": str(countrie.name),
            "image": str(countrie.image),

 }

