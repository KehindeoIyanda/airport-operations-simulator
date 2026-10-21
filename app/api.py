

from flask import Flask, jsonify

app = Flask(__name__)

# Fictional flight information for learning purposes
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
    }

]

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Airport Operations Backend Simulator",
        "status": "Online"
    })

@app.route("/flights")
def get_flights():
    return jsonify(flights)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)