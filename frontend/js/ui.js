// frontend/js/ui.js

import { analyzeData } from './api.js';
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
    // PERBAIKAN UTAMA: Mencegah halaman me-refresh secara paksa.
    event.preventDefault(); 

    const file = elements.fileInput.files[0];
    if (!file) {
        showError('Please choose a CSV file first!');
        return;
    }

    showLoading(true);

    try {
        const result = await analyzeData(file);
        displayResults(result);
    } catch (err) {
        showError(err.message);
    } finally {
        showLoading(false);
    }
}

function showLoading(isLoading) {
    elements.loadingDiv.classList.toggle('hidden', !isLoading);
    elements.resultsDiv.classList.add('hidden');
    elements.errorDiv.classList.add('hidden');
}

function displayResults(data) {
    elements.resultsDiv.classList.remove('hidden');
    elements.equationP.innerHTML = `<strong>Regression Equation:</strong> ${data.equation}`;
    const ctx = elements.chartCanvas.getContext('2d');
    displayChart(ctx, data);
}

function showError(message) {
    elements.errorDiv.classList.remove('hidden');
    elements.errorMessageP.textContent = `Error: ${message}`;
    elements.resultsDiv.classList.add('hidden');
}

/**
 * Mengatur semua event listener untuk halaman.
 */
export function setupEventListeners() {
    elements.fileInput.addEventListener('change', () => {
        elements.fileNameSpan.textContent = elements.fileInput.files.length > 0 ? elements.fileInput.files[0].name : 'No file chosen';
    });

    // Pastikan fungsi handleAnalysis menerima 'event'
    elements.analyzeButton.addEventListener('click', handleAnalysis);
}