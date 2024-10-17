def new_airport(airport_dictionary):
    key = input("Enter new airport ICAO: ")
    value = input("Enter new airport name: ")
    airport_dictionary[key] = value
    input("New airport has been saved. Press enter to continue!")
    return airport_dictionary

def fetch_airport(airport_dictionary):
    key = input("Enter airport ICAO: ")
    if key in airport_dictionary:
        print(f"Your aiport name with ICAO code {key} is {airport_dictionary[key]}.")
        input("Press Enter to continue!")
    else:
        print("Data not found!")

def print_menu():
    print("\nMain menu, please enter number of the action: ")
    print(" 1. Enter new airport.")
    print(" 2. Fetch information of existing airport.")
    print(" 3. Exit.")
    return input()
#main

airport = {
    "EFHK":"Helsinki-Vantaa",
    "LIML":"Linate",
    "LFPG":"Charles De Gaulle",
    "EDDM":"Franz Josef Strauss"
}
state = "0"
while True:
    if state == "0":
        state = print_menu()
    elif state == "1":
        new_airport(airport)
        state = "0"
    elif state == "2":
        fetch_airport(airport)
        state = "0"
    elif state == "3":
        print("Exit script, thank you!")
        break
    else:
        print("Invalid input!")
        state = "0"