// frontend/js/api.js
// Alamat API backend
const API_URL = 'http://127.0.0.1:5000/api/analyze';

/**
 * Mengirim file CSV ke backend untuk dianalisis.
 * @param {File} file - File CSV yang akan diunggah.
 * @returns {Promise<Object>} - Sebuah promise yang akan resolve dengan hasil analisis.
 */
export async function analyzeData(file) {
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch(API_URL, {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();

    if (!response.ok) {
        // Jika backend mengirim error, lemparkan error tersebut agar bisa ditangkap
        throw new Error(result.error || 'An unknown server error occurred.');
    }

    return result;
}