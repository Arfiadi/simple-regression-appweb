// frontend/js/ui.js

import { analyzeData, checkServerHealth } from './api.js';
import { displayChart } from './chart.js';

const elements = {
    fileInput: document.getElementById('csvFileInput'),
    analyzeButton: document.getElementById('analyzeButton'),
    fileNameSpan: document.getElementById('fileName'),
    resultsDiv: document.getElementById('results'),
    equationP: document.getElementById('equation'),
    loadingDiv: document.getElementById('loading'),
    errorDiv: document.getElementById('error'),
    errorMessageP: document.getElementById('errorMessage'),
    chartCanvas: document.getElementById('regressionChart'),
};

/**
 * Menangani logika utama saat tombol "Analyze" diklik.
 * @param {Event} event - Objek event dari klik tombol.
 */
async function handleAnalysis(event) {
    event.preventDefault();
    
    console.log("Analyze button clicked");

    const file = elements.fileInput.files[0];
    if (!file) {
        showError('Please choose a CSV file first!');
        return;
    }

    console.log("File selected:", file.name);

    // Validasi ekstensi file di frontend
    if (!file.name.toLowerCase().endsWith('.csv')) {
        showError('Please upload a CSV file (.csv extension)');
        return;
    }

    // PERBAIKAN: Cek koneksi server terlebih dahulu
    showLoading(true);
    console.log("Checking server connection...");
    
    const isServerRunning = await checkServerHealth();
    if (!isServerRunning) {
        showLoading(false);
        showError('Cannot connect to the backend server. Please make sure the Flask server is running on http://127.0.0.1:5000');
        return;
    }

    console.log("Server is running, proceeding with analysis...");

    try {
        const result = await analyzeData(file);
        console.log("Analysis result received:", result);
        displayResults(result);
    } catch (err) {
        console.error("Error during analysis:", err);
        showError(err.message);
    } finally {
        showLoading(false);
    }
}

/**
 * Menampilkan atau menyembunyikan loading indicator
 */
function showLoading(isLoading) {
    console.log("Show loading:", isLoading);
    
    if (isLoading) {
        elements.loadingDiv.classList.remove('hidden');
        elements.resultsDiv.classList.add('hidden');
        elements.errorDiv.classList.add('hidden');
        elements.analyzeButton.disabled = true;
    } else {
        elements.loadingDiv.classList.add('hidden');
        elements.analyzeButton.disabled = false;
    }
}

/**
 * Menampilkan hasil analisis
 */
function displayResults(data) {
    console.log("Displaying results");
    
    elements.resultsDiv.classList.remove('hidden');
    elements.errorDiv.classList.add('hidden');
    elements.equationP.innerHTML = `<strong>Regression Equation:</strong> ${data.equation}`;
    
    const ctx = elements.chartCanvas.getContext('2d');
    displayChart(ctx, data);
}

/**
 * Menampilkan pesan error
 */
function showError(message) {
    console.error("Showing error:", message);
    
    elements.errorDiv.classList.remove('hidden');
    elements.resultsDiv.classList.add('hidden');
    elements.errorMessageP.textContent = `Error: ${message}`;
}

/**
 * Reset tampilan file input
 */
function resetFileInput() {
    elements.fileNameSpan.textContent = 'No file chosen';
}

/**
 * Mengatur semua event listener untuk halaman.
 */
export function setupEventListeners() {
    console.log("Setting up event listeners");
    
    // Event listener untuk file input
    elements.fileInput.addEventListener('change', (event) => {
        console.log("File input changed");
        const files = event.target.files;
        
        if (files.length > 0) {
            elements.fileNameSpan.textContent = files[0].name;
            console.log("File selected:", files[0].name);
        } else {
            resetFileInput();
        }
        
        // Reset error dan hasil sebelumnya
        elements.errorDiv.classList.add('hidden');
        elements.resultsDiv.classList.add('hidden');
    });

    // Event listener untuk tombol analyze
    elements.analyzeButton.addEventListener('click', handleAnalysis);
    
    console.log("Event listeners set up successfully");
}