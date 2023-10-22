# backend/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/message')
def get_message():
    return jsonify({'message': 'Hello from the backend!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Bind to '0.0.0.0' to listen on all available network interfaces

# get into http://192.168.8.102:5000/api/message