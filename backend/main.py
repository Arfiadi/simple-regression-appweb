# backend/main.py
from flask import Flask, jsonify
from flask_cors import CORS

# Inisialisasi aplikasi Flask
app = Flask(__name__)
# CORS (Cross-Origin Resource Sharing) penting agar frontend
# yang berjalan di domain berbeda bisa berkomunikasi dengan backend ini
CORS(app)

@app.route('/api/status', methods=['GET'])
def get_status():
    """Endpoint sederhana untuk memeriksa apakah server berjalan."""
    return jsonify({"status": "Backend server is running successfully!"}), 200

if __name__ == '__main__':
    # host='0.0.0.0' penting agar server bisa diakses dari luar container Docker nanti
    app.run(host='0.0.0.0', port=5000, debug=True)