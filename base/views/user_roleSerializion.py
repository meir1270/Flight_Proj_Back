from rest_framework import serializers
from base.models import User_Role

class User_Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Role
        fields = '__all__'

    def get_User_Role(self,obj):
        return {
            "name_role": str(obj.name_role),
            }


    def get_All_User_Role(self):
        res=[] #create an empty list
        for User_Role_Obj in User_Role.objects.all(): #run on every row in the table...
            res.append(self.get_User_Role(User_Role_Obj)) #append row by to row to res list
        return res


    def get_User_Role_By_Id(self,id):
        user_role= User_Role.objects.get(_id = id)
        return {
            "id": user_role._id,
            "name_role": str(user_role.name_role),
            }
