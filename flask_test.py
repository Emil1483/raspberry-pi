from gpiozero import LED
from flask import Flask, request

app = Flask(__name__)

led = LED(14)

@app.route("/led", methods=["POST"])
def toggle_led():
    led.toggle()
    return "OK"

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
