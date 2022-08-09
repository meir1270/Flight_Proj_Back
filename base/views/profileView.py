from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated 
from base.views.profileSerializion  import ProfileSerializer
from base.models import UserProfile

 
@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def getUserProfile(request,id=-1):
    user = request.user
    print(user,"innnn")
    if request.method == 'DELETE': #method delete a row
        temp= UserProfile.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    if int(id) > -1: #get single product
        return JsonResponse(ProfileSerializer().get_UserProfile_By_Id(id),safe=False)
    else: # return all
        return JsonResponse(ProfileSerializer().get_All_UserProfile(),safe=False) #return array as json response

 
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def addUserProfile(request):
#     print(request.data)
#     user = request.user
#     UserProfile.objects.create(
#         name=request.data["name"],
#         user=user,
#         countrie=UserProfile.objects.get(_id=request.data['countrie_Id']))
#     print(user)
#     return JsonResponse({'POST':"success"})
 


