#Write a Car class that has the following properties:
#registration number, maximum speed, current speed and travelled distance.
##Add a class initializer that sets the first two of the properties based on parameter values.
#the current speed and travelled distance of a new car must be automatically set to zero.
#Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
#Finally, print out all the properties of the new car.
class car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0



Car = car("ABC123",140)

print(f"Information of the car is:\nCar registation {Car.registration_number}"
      f"\nMaximum speed {Car.maximum_speed}"
      f"\nCurrent speed {Car.current_speed}"
      f"\nTravelled distance {Car.travelled_distance}")
