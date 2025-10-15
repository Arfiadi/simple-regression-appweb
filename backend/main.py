# backend/main.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
import traceback

# Impor fungsi analisis dari pustaka Matriks Anda
from regression.linear_regression import perform_linear_regression

app = Flask(__name__)
# PERBAIKAN: Konfigurasi CORS yang lebih spesifik
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Konfigurasi folder upload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/analyze', methods=['POST'])
def analyze_data():
    try:
        # 1. Validasi request file
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # 2. Validasi ekstensi file
        if not file.filename.lower().endswith('.csv'):
            return jsonify({"error": "Unsupported file format. Please upload a .csv file"}), 400

        # 3. Simpan dan proses file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        print(f"File saved to: {filepath}")  # Debug log
        
        # 4. Baca dan validasi CSV
        df = pd.read_csv(filepath)
        print(f"CSV shape: {df.shape}")  # Debug log
        print(f"CSV columns: {df.columns.tolist()}")  # Debug log
        
        if df.shape[1] != 2:
            os.remove(filepath)
            return jsonify({"error": f"CSV file must have exactly 2 columns. Found {df.shape[1]} columns."}), 400

        if df.shape[0] < 2:
            os.remove(filepath)
            return jsonify({"error": "CSV file must have at least 2 rows of data."}), 400

        # 5. Panggil fungsi analisis
        print("Starting linear regression analysis...")  # Debug log
        analysis_result = perform_linear_regression(df)
        print("Analysis completed successfully")  # Debug log
        
        # 6. Hapus file setelah diproses
        os.remove(filepath)
        
        # 7. Kembalikan hasil sebagai JSON
        return jsonify(analysis_result), 200

    except pd.errors.EmptyDataError:
        return jsonify({"error": "CSV file is empty"}), 400
    except pd.errors.ParserError:
        return jsonify({"error": "Unable to parse CSV file. Please check the file format."}), 400
    except Exception as e:
        # Log error lengkap untuk debugging
        print("Error occurred:")
        print(traceback.format_exc())
        return jsonify({"error": f"An error occurred during analysis: {str(e)}"}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint untuk mengecek apakah server berjalan"""
    return jsonify({"status": "ok", "message": "Server is running"}), 200

if __name__ == '__main__':
    print("Starting Flask server...")
    print(f"Upload folder: {UPLOAD_FOLDER}")
    app.run(host='0.0.0.0', port=5000, debug=True)