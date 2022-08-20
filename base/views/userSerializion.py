from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
 
    def getUserName(self,obj):
        return obj.username
 
    def getUser(self,obj):
        print(obj)
        if obj == None: return {}
        return {
            "id": obj.id,
            "username":obj.username,
            "email":   obj.email
            }

