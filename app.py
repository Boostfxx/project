from flask import Flask, render_template, request
from gpiozero import LED
from threading import Lock

app = Flask(__name__)
led = LED(23)
gpio_lock = Lock()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle-led', methods=['POST'])
def toggle_led():
    global led
    with gpio_lock:
        if led.is_lit:
            led.off()
        else:
            led.on()
    return ('', 204)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, threaded=True)
    finally:
        led.close()

