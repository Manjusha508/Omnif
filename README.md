Project:Omnify
Appname:fitness

Postman Urls:

List of classes:
http://127.0.0.1:8000/api/classes/

To create fitness classes:
http://127.0.0.1:8000/api/classes/create/

{
  "name": "Yoga Basics",
  "instructor": "Alice Smith",
  "date_time": "2025-06-10",
  "available_slots": 20
}

To delete the fitness clasess:
http://127.0.0.1:8000/api/classes/7/

To list all the bookings booked w.r.t to instructor:
http://127.0.0.1:8000/api/bookings/

To book or create under instrucor for fitness:
http://127.0.0.1:8000/api/book/

{
  "fitness_class": 2,
  "client_name": "Jane Doe",
  "client_email": "jane.doe@example.com"
}


To delete the bookings:
http://127.0.0.1:8000/api/booking/delete/5/


Postgresql-->Database:Fitness

Fitness:
SELECT * FROM public.fitness_fitness ORDER BY id ASC 

Bookings:
SELECT * FROM public.fitness_booking ORDER BY id ASC 
