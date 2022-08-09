from django.urls import path
from .views import customerView, adminstratorView,countrieView,airline_CompanieView,flightView,ticketsView,profileView
from .views.customerView import MyTokenObtainPairView
from .views.adminstratorView import MyTokenObtainPairView
from .views.countrieView import MyTokenObtainPairView
from .views.airline_CompanieView import MyTokenObtainPairView
from .views.flightView import MyTokenObtainPairView
from .views.ticketsView import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static
 
urlpatterns = [
    # customers urls:
    path('customers', customerView.getCustomer),
    path('customers/<id>', customerView.getCustomer),
    path('addcustomer', customerView.addCustomer),
    # adminstrator urls:
    path('adminstrator', adminstratorView.getAdminstrator),
    path('adminstrator/<id>', adminstratorView.getAdminstrator),
    path('addadminstrator', adminstratorView.addAdminstrator),
    # countrie urls:
    path('countrie', countrieView.getCountrie),
    path('countrie/<id>', countrieView.getCountrie),
    path('addcountrie', countrieView.addCountrie),
    # airline_Companie urls:
    path('airline_Companie', airline_CompanieView.getAirline_Companie),
    path('airline_Companie/<id>', airline_CompanieView.getAirline_Companie),
    path('addairline_Companie', airline_CompanieView.addAirline_Companie),
    # Flight urls:
    path('flight', flightView.getFlight),
    path('flight/<id>', flightView.getFlight),
    path('addflight', flightView.addFlight),
    path('deleteflight/<id>', flightView.deleteFlight),
    path('selectflight/<origin_countrie>/<destination_countrie>/<departure_time>/<landing_time>', flightView.get_filght_by_filters),
    # Tickets urls:
    path('tickets', ticketsView.getTickets),
    path('usertickets', ticketsView.getTicketsForUSER),
    path('tickets/<id>', ticketsView.getTickets),
    path('addtickets', ticketsView.addTickets),
    # get token urls:
    # login url:
    path('token/', customerView.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # refresh url
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # register/SignUp url:
    path('adduser', customerView.addUser),
    # Logout
    path('logout', customerView.logout_view),
    # Users url:
    path('users', profileView.getUserProfile),
    path('users/<id>', profileView.getUserProfile),
]


# add a image to static folder 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 

