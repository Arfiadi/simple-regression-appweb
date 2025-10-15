// frontend/js/api.js

// The address of your backend API
const API_URL = 'http://127.0.0.1:5000/api/analyze';

/**
 * Sends a CSV file to the backend for analysis.
 * @param {File} file - The CSV file to upload.
 * @returns {Promise<Object>} - A promise that resolves with the analysis result.
 */
export async function analyzeData(file) {
    console.log("Starting analyzeData function");
    console.log("File details:", {
        name: file.name,
        size: file.size,
        type: file.type
    });

    const formData = new FormData();
    formData.append('file', file);

    try {
        console.log("Sending request to:", API_URL);
        
        const response = await fetch(API_URL, {
            method: 'POST',
            body: formData,
            // PERBAIKAN: Tambahkan mode dan credentials jika diperlukan
            mode: 'cors',
        });

        console.log("Response status:", response.status);
        console.log("Response ok:", response.ok);

        const result = await response.json();
        console.log("Response data:", result);

        if (!response.ok) {
            // If the backend returns an error, throw it so it can be caught
            throw new Error(result.error || 'An unknown server error occurred.');
        }

        return result;
        
    } catch (error) {
        console.error("Error in analyzeData:", error);
        
        // PERBAIKAN: Berikan pesan error yang lebih deskriptif
        if (error.message.includes('Failed to fetch')) {
            throw new Error('Cannot connect to server. Please make sure the backend is running on http://127.0.0.1:5000');
        }
        
        throw error;
    }
}

/**
 * Check if the backend server is running
 * @returns {Promise<boolean>}
 */
export async function checkServerHealth() {
    try {
        const response = await fetch('http://127.0.0.1:5000/api/health');
        return response.ok;
    } catch (error) {
        console.error("Server health check failed:", error);
        return false;
    }
}