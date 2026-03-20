
from abc import ABC,abstractmethod
class Vehicle(ABC):
   def __init__(self,brand,base_price_per_day,Return_vehicle ):
       self.brand=brand
       self.__price=base_price_per_day
       self.available=Return_vehicle
       

   def get_price(self):
       return self.__price
   @abstractmethod
   def calculate_rent(self,days):
      pass
   def rent(self):
    if not self.available:
       print(f"{self.brand} renting Unavailable Vehicle ")
    else:
      self.available = True
      print(f"{self.brand}  Rent Available Vehicle ")
   
class Car(Vehicle):
  def calculate_rent(self, days,total_rent):
    if not self.available:
       print(f"{self.brand} - Car Not available")
    else:  
       total_rent=self.get_price() * days
       print(f" {self.brand} - Car available base_price_per_day: {self.get_price()}")
       return total_rent
       

class Bike(Vehicle):
  def calculate_rent(self, days,total_rent):
    if not self.available:
       print(f"{self.brand} - Bike Not available")
    else:
        total_rent=self.get_price() * days * 0.8
        print(f" {self.brand} - Bike available base_price_per_day: {self.get_price()}")
        return total_rent


class Truck(Vehicle):
  def calculate_rent(self, days,total_rent):
    if not self.available:
       print(f"{self.brand} - Truck Not available")
    else:
     total_rent=self.get_price() * days * 1.1
     print(f" {self.brand} - Truck available base_price_per_day: {self.get_price()}")
     return total_rent



v1=Car("Toyota",2000,Return_vehicle=(True))
v2=Bike("MT-15",1000,Return_vehicle=(True))
v3= Truck("Tata",3000,Return_vehicle=(True))

v1.rent()
v2.rent()
v3.rent()

vehicles=[v1,v2,v3]


print("Rental cost")
days=5
total_rent=0


for v in vehicles:
  cost=v.calculate_rent(days,total_rent)
  
  print(f"{v.brand} Rent for Days {days} Total Rent={cost}")
