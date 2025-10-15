// The address of your backend API
const API_URL = 'http://127.0.0.1:5000/api/analyze';

/**
 * Sends a CSV file to the backend for analysis.
 * @param {File} file - The CSV file to upload.
 * @returns {Promise<Object>} - A promise that resolves with the analysis result.
 */
export async function analyzeData(file) {
    console.log("4. Function analyzeData in api.js is running."); // Debugging log

    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch(API_URL, {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();

    if (!response.ok) {
        // If the backend returns an error, throw it so it can be caught
        throw new Error(result.error || 'An unknown server error occurred.');
    }

    return result;
}