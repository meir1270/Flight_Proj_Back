from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 
from base.views.countrieSerializion import CountrieSerializer
from base.models import Countrie
 
 
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
def getCountrie(request,id=-1):
    user = request.user
    print(user,"innnn")
    if int(id) > -1: #get single product
        return JsonResponse(CountrieSerializer().get_Countrie_By_Id(id),safe=False)
    else: # return all
        return JsonResponse(CountrieSerializer().get_All_Countrie(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCountrie(request):
    print(request.data)
    user = request.user
    Countrie.objects.create(
        name=request.data["name"],
        image=request.data["image"])
    print(user)
    return JsonResponse({'POST':"success"})
 
 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCountrie(request,id=-1):
        temp= Countrie.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})


