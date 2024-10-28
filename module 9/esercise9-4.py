
from random import randint
import prettytable
from prettytable import PrettyTable


class Car:
    current_speed = 0
    travelled_distance = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

    def accelerate(self, acceleration):
        self.current_speed += acceleration
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance = self.travelled_distance + self.current_speed * hours


car_list = []
finish_flag = -1
hour_passed = 0
cars_cur_travelled_distanced = []

table = PrettyTable() #creates the table and the headers of the table
field_names = ["Hour pass"]#adds the first column of the table
for i in range(0,10):
    car_name = "BRK-78"+str(i)
    car_list.append(Car(car_name, randint(100,200)))
    field_names.append(car_name)##adds the ramaining table in the table basically the reg number.

table.field_names = field_names ## adds the field name into the table
while finish_flag != 1:
    hour_passed += 1
    cars_cur_travelled_distanced.append(hour_passed)

    for i in range(0,10):
        car_list[i].accelerate(randint(-10,15))
        car_list[i].drive(1)
        if car_list[i].travelled_distance >= 10000:
            finish_flag = 1
        cars_cur_travelled_distanced.append(car_list[i].travelled_distance)

    table.add_row(cars_cur_travelled_distanced)
    cars_cur_travelled_distanced.clear()

print("Travelled distance of cars during race")
print(table)
print(f"The winning car is {car_list[finish_flag].registration_number}")
