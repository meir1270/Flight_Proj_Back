from rest_framework.serializers import ModelSerializer
from base.models import Customer
from base.views.userSerializion import UserSerializer
 
 
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def get_Customer(self,obj):
        return {
            "id": obj._id,
            "first_name": str(obj.first_name),
            "last_name": obj.last_name,
            "address": obj.address,
            "phone_No": obj.phone_No,
            "createdTime": obj.createdTime,
            "user": UserSerializer().getUser(obj.user)
            }

    def get_All_Customer(self):
        res=[] #create an empty list
        for customerObj in Customer.objects.all(): #run on every row in the table...
            res.append(self.get_Customer(customerObj)) #append row by to row to res list
        return res


    def get_Customer_By_Id(self,id):
        customer= Customer.objects.get(_id = id)
        return {
            "id": customer._id,
            "first_name": str(customer.first_name),
            "last_name": str(customer.last_name),
            "address": str(customer.address),
            "phone_No": str(customer.phone_No),
            "createdTime": customer.createdTime,
            "user": UserSerializer().getUser(customer.user)
            }

