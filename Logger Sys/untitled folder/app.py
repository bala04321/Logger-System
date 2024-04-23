#Code by Nallapati Bala Yashaswini
from flask import Flask, jsonify, request
from logger import Logger

app = Flask(__name__)
logger = Logger()

@app.route('/log', methods=['POST'])
def log_event():
    data = request.json
    if logger.log(data['timestamp'], data['severity'], data['message']):
        return jsonify({'status': 'Log added'}), 201
    else:
        return jsonify({'error': 'Logging not allowed outside operating hours'}), 403

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logger.get_logs()), 200

if __name__ == '__main__':
    app.run(debug=True)
