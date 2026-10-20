
# Airport Operations Backend Simulator
# This program displays fictional airport flight information.

flights = [
    {
        "flight_number": "FL101",
        "destination": "Chicago",
        "gate": "A1",
        "status": "On Time",
    },
    {
        "flight_number": "FL202",
        "destination": "Denver",
        "gate": "A2",
        "status": "Boarding",
    },
    {
        "flight_number": "FL303",
        "destination": "Dallas",
        "gate": "B1",
        "status": "Delayed",
    },
]


print("===============================")
print(" AIRPORT DEPARTURE INFORMATION")
print("===============================")


for flight in flights:

    print(f"Flight: {flight['flight_number']}")
    print(f"Destination: {flight['destination']}")
    print(f"Gate: {flight['gate']}")
    print(f"Status: {flight['status']}")
    print("--------------------------------------")
