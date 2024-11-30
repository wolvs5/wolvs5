from flask import Flask, jsonify
import math

app = Flask(__name__)

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Endpoint to check if a number is prime
@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    prime_status = is_prime(number)
    return jsonify({"Number": number, "isPrime": prime_status})

# Sample airport data (in a real application, this would be in a database)
airport_data = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Location": "London"},
    "KATL": {"Name": "Hartsfield-Jackson Atlanta International Airport", "Location": "Atlanta"},
    # Add more airports as needed
}

# Endpoint to get airport information by ICAO code
@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport(icao_code):
    airport = airport_data.get(icao_code)
    if airport:
        return jsonify({"ICAO": icao_code, "Name": airport["Name"], "Location": airport["Location"]})
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)