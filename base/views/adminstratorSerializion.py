from rest_framework.serializers import ModelSerializer
from base.models import Adminstrator
from base.views.userSerializion import UserSerializer
 
 
class AdminstratorSerializer(ModelSerializer):
    class Meta:
        model = Adminstrator
        fields = '__all__'

    def get_Adminstrator(self,obj):
        return {
            "id": obj._id,
            "first_name": str(obj.first_name),
            "last_name": obj.last_name,
            "createdTime": obj.createdTime,
            "user": UserSerializer().getUser(obj.user)
            }

    def get_All_Adminstrator(self):
        res=[] #create an empty list
        for adminstratorObj in Adminstrator.objects.all(): #run on every row in the table...
            res.append(self.get_Adminstrator(adminstratorObj)) #append row by to row to res list
        return res


    def get_Adminstrator_By_Id(self,id):
        adminstrator= Adminstrator.objects.get(_id = id)
        return {
            "id": adminstrator._id,
            "first_name": str(adminstrator.first_name),
            "last_name": adminstrator.last_name,
            "createdTime": adminstrator.createdTime,
            "user": UserSerializer().getUser(adminstrator.user)
            }

