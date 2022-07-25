from rest_framework.serializers import ModelSerializer
from base.models import UserProfile
from base.views.userSerializion import UserSerializer
from base.views.user_roleSerializion import User_Role_Serializer
 
 
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def get_UserProfile(self,obj):
        return {
            "id": obj._id,
            "user": UserSerializer().getUser(obj.user),
            "user_role": User_Role_Serializer().get_User_Role(obj.user_role)
            }

    def get_All_UserProfile(self):
        res=[] #create an empty list
        for Obj in UserProfile.objects.all(): #run on every row in the table...
            res.append(self.get_UserProfile(Obj)) #append row by to row to res list
        return res


    def get_Customer_By_Id(self,id):
        profile= UserProfile.objects.get(_id = id)
        return {
            "id": profile._id,
            "user": UserSerializer().getUser(profile.user),
            "user_role": User_Role_Serializer().get_User_Role(profile.user_role)
            }

