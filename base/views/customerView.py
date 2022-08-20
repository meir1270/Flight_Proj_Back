from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from base.views.customersSerializion import CustomerSerializer
from base.models import Customer,UserProfile
from django.contrib.auth import logout

 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
 
# Register
@api_view(['POST'])
def addUser(request):
    user = User.objects.create_user(username=request.data['username'],
                                 email=request.data['email'],
                                 password=request.data['pwd'])
    UserProfile.objects.create(user=user,user_role_id=1)
    return JsonResponse({"user created":request.data['username']} )

# logout
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    print(request.user, "logged out")
    logout(request) 
    return JsonResponse("user Logout",safe=False)

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def getCustomer(request,id=-1):
    user = request.user
    print(user,"innnn")
    if request.method == 'DELETE': #method delete a row
        temp= Customer.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if int(id) > -1: #get single Customer
        return JsonResponse(CustomerSerializer().get_Customer_By_Id(id),safe=False)
    else: # return all
        return JsonResponse(CustomerSerializer().get_All_Customer(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCustomer(request):
    print(request.data)
    user = request.user
    Customer.objects.create(
        first_name=request.data["first_name"],
        last_name=request.data["last_name"],
        address=request.data["address"],
        phone_No=request.data["phone_No"],
        credit_card_No=request.data["credit_card_No"],
        user=user)
    return JsonResponse({"post":"succsess"})
 
 


