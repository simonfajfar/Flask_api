import os
from flask import Flask, render_template

app = Flask(__name__)

count = 0
uporabniki = [
    {"ime": "Uros", "priimek": "Jarc"},
    {"ime": "Uros", "priimek": "Jarc"},
]

@app.route("/", methods=['GET'])
def index():
    global count
    count += 1
    return render_template('index.html', naslov= 'Živijo')

@app.route("/biografija", methods=['GET'])
def biografija():
    global count
    count += 1
    return render_template('biografija.html')

@app.route("/stevilo-uporabnikov", methods=['GET'])
def stevilo_uporabnikov():
    global count
    global uporabniki
    count += 1
    return render_template('stevilo_uporabnikov.html', count = count, uporabniki = uporabniki)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
