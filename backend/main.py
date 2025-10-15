# backend/main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os

# Impor fungsi analisis dari pustaka Matriks Anda
from regression.linear_regression import perform_linear_regression

app = Flask(__name__)
CORS(app)

# Konfigurasi folder upload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    # 1. Validasi request file
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # 2. Proses file
    if file and file.filename.endswith('.csv'):
        try:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # 3. Baca dan lakukan analisis
            df = pd.read_csv(filepath)
            
            if df.shape[1] != 2:
                os.remove(filepath) # Hapus file sebelum kirim error
                return jsonify({"error": "CSV file must have exactly 2 columns"}), 400

            # Panggil "otak" analisis Anda
            analysis_result = perform_linear_regression(df)
            
            # 4. Hapus file setelah diproses
            os.remove(filepath)
            
            # 5. Kembalikan hasil sebagai JSON
            return jsonify(analysis_result)

        except Exception as e:
            # Jika terjadi error selama perhitungan, kirim pesan yang jelas
            return jsonify({"error": f"An error occurred during analysis: {str(e)}"}), 500
    
    return jsonify({"error": "Unsupported file format. Please upload a .csv file"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)