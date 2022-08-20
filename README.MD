# Flight Project Back

### About / usage
- flight management system that allows airline companies to advertise flights  <br/> 
and for customers to choose the one that suits them the best at an attractive price.

- This project is the final project in my studies. <br/>
    i will be using Django as logic,<br/>
    React redux toolkit to view front (GUI)<br/>
    sqlite3 as sql database.<br/>


- Project status: finish <br/>
  i start in 29/06/2022 ,and finish in 29/8/2022.<br/>

### DATABASE/MODELS

- Customer:
    id (PK)(AI)
    first name 
    last name
    address 
    phone number (U)
    credit card number (U)        
    user (FK)
    createdTime

- Adminstrator:
    id (PK)(AI)
    first name
    last name
    user (FK)
    createdTime
    
- Countrie:
    id (PK)(AI)
    name - 
    image - State flag

- Airline Companie:
    id (PK)(AI)
    name(U)
    user (FK)
    countrie (FK) 
    createdTime

-Flight:
    id (PK)(AI)
    airline Companie (FK) 
    origin countrie (FK)
    destination countrie (FK)
    departure time
    landing time
    remaining tickets 
    status

- Tickets:
    id (PK)(AI)
    flight (FK)(U)
    customer (FK)(U) 

- User_Role:
    id (PK)(AI)
    name role: Customer/airline/manager


### urls - http://127.0.0.1:8000
- /customers (to show all customers)
- /customers/id (to show customer by id)
- /addcustomer (to add customer)
- /adminstrator (to show all adminstrators)
- /adminstrator/id (to show adminstrator by id)
- /addadminstrator (to add adminstrator)
- /countrie (to show all countries)
- /countrie/id (to show countrie by id)
- /addcountrie (to add countrie)
- /airline_Companie (to show all airline Companies)
- /airline_Companie/id (to show  airline_Companie by id) 
- /addairline_Companie  (to add airline Companie)
- /flight (to show all flights)
- /flight/id (to show flight by id)
- /addflight (to add  flight)
- /tickets  (to show all tickets)
- /tickets/id  (to show  tickets by id)
- /addtickets (to add tickets)
- /token (Login)
- /token/refresh/ (to refresh a token)
- /adduser (register/SginUp)
- /logout (Logout)
### Requirements
I added requirements.txt there you can see all the packages i used in this project.<br/>
to install them "Pip install -r requirements.txt" <br/>
to start the project "python manage.py runserver" <br/>