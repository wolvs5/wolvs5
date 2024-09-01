#Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.
se= (input("are you male or female? "))
while se == "":
    print("you haven't entered anything")
    input("are you male or female")

if se == "male":
      value=int(input("how much is your hemoglobin"))
      if value<=135:
           print("your hemoglobin is low")
      elif value>=168:
           print("your hemoglobin is high")
      else:
           print("it is normal")
elif se == "female":
      value=int(input("how much is your hemoglobin"))
      if value<=116:
            print("your hemoglobin is low")
      elif value>=156:
           print("your hemoglobin is high")
      else:
           print("it is normal")


