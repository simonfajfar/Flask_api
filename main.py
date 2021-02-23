import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', naslov= 'Živijo')

@app.route("/biografija", methods=['GET'])
def biografija():
    return render_template('biografija.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host='0.0.0.0')





