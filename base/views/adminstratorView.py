from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
 
from base.views.adminstratorSerializion import AdminstratorSerializer
from base.models import Adminstrator
 
 
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
def getAdminstrator(request,id=-1):
    if request.method == 'DELETE': #method delete a row
        temp= Adminstrator.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    user = request.user
    print(user,"innnn")
    if int(id) > -1: #get single product
        return JsonResponse(AdminstratorSerializer().get_Adminstrator_By_Id(id),safe=False)
    else: # return all
        return JsonResponse(AdminstratorSerializer().get_All_Adminstrator(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAdminstrator(request):
    print(request.data)
    user = request.user
    Adminstrator.objects.create(
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        user=user)
    print(user)
    return JsonResponse({'POST':"success"})
 
 

