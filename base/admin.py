from django.contrib import admin
from .models import Customer,Countrie,Adminstrator,Airline_Companie,Flight,Tickets,User_Role,UserProfile
 
admin.site.register(Customer)
admin.site.register(Countrie)
admin.site.register(Adminstrator)
admin.site.register(Airline_Companie)
admin.site.register(Flight)
admin.site.register(Tickets)
admin.site.register(User_Role)
admin.site.register(UserProfile)
