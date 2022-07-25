# Flight Project

### About / usage
- This project is the final project in my studies. <br/>
    i will be using Django as logic,<br/>
    React JS to view front (GUI)<br/>
    sqlite3 as sql database.<br/>


- Project status: working/prototype <br/>
  i start in 29/07/2002 ,now It's currently a working.<br/>

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


### urls
- http://127.0.0.1:8000/customers (to show all customers)
- http://127.0.0.1:8000/customers/id (to show customer by id)
- http://127.0.0.1:8000/addcustomer (to add customer)
- http://127.0.0.1:8000/adminstrator (to show all adminstrators)
- http://127.0.0.1:8000/adminstrator/id (to show adminstrator by id)
- http://127.0.0.1:8000/addadminstrator (to add adminstrator)
- http://127.0.0.1:8000/countrie (to show all countries)
- http://127.0.0.1:8000/countrie/id (to show countrie by id)
- http://127.0.0.1:8000/addcountrie (to add countrie)
- http://127.0.0.1:8000/airline_Companie (to show all airline Companies)
- http://127.0.0.1:8000/airline_Companie/id (to show  airline_Companie by id) 
- http://127.0.0.1:8000/addairline_Companie  (to add airline Companie)
- http://127.0.0.1:8000/flight (to show all flights)
- http://127.0.0.1:8000/flight/id (to show flight by id)
- http://127.0.0.1:8000/addflight (to add  flight)
- http://127.0.0.1:8000/tickets  (to show all tickets)
- http://127.0.0.1:8000/tickets/id  (to show  tickets by id)
- http://127.0.0.1:8000/addtickets (to add tickets)
- http://127.0.0.1:8000/token (to get a token)
- http://127.0.0.1:8000/token/refresh/ (to refresh a token)
- http://127.0.0.1:8000/adduser (register/SginUp)
### Requirements
I added requirements.txt there you can see all the packages i used in this project.<br/>
to install them "Pip install -r requirements.txt"