#Extend the program by adding an accelerate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed.
# The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h,
# \then +70 km/h and finally +50 km/h. Then print out the current speed of the car.
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and
#then print out the final speed.
#The travelled distance does not have to be updated yet.
from random import randint
class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, acceleration):
        self.current_speed += acceleration
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

reg_num = "ABC-123"
max_speed = 140

car = Car(reg_num, max_speed)

print(f"Information of the car is:\nCar registation {car.registration_number}"
      f"\nMaximum speed {car.maximum_speed}"
      f"\nCurrent speed {car.current_speed}"
      f"\nTravelled distance {car.travelled_distance}\n")
print(f"Acceleration... Current speed {car.current_speed}")
car.accelerate(30)
print(f"Acceleration... Current speed {car.current_speed}")
car.accelerate(70)
print(f"Acceleration... Current speed {car.current_speed}")
car.accelerate(50)
print(f"Acceleration... Current speed {car.current_speed}")
car.accelerate(-200)
print(f"Emergency brake... Current speed {car.current_speed}")
