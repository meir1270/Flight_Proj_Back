from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 
from base.views.airline_CompanieSerializion  import Airline_CompanieSerializer
from base.models import Airline_Companie, Countrie
 
 
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
 
 
 
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def getAirline_Companie(request,id=-1):
    user = request.user
    print(user,"innnn")
    if request.method == 'DELETE': #method delete a row
        temp= Airline_Companie.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if int(id) > -1: #get single product
        return JsonResponse(Airline_CompanieSerializer().get_Airline_Companie_By_Id(id),safe=False)
    else: # return all
        return JsonResponse(Airline_CompanieSerializer().get_All_Airline_Companie(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAirline_Companie(request):
    print(request.data)
    user = request.user
    Airline_Companie.objects.create(
        name=request.data["name"],
        user=user,
        countrie=Countrie.objects.get(_id=request.data['countrie_Id']))
    print(user)
    return JsonResponse({'POST':"success"})
 


