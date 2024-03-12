from flask import Flask, render_template, request
from gpiozero import LED
from threading import Lock

app = Flask(__name__)
cat = LED(23)
gpio_lock = Lock()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle-cat', methods=['POST'])
def toggle_cat():
    global cat
    with gpio_lock:
        if cat.is_lit:
            cat.off()
        else:
            cat.on()
    return ('', 204)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, threaded=True)
    finally:
        cat.close()

