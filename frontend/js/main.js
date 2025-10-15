import { setupEventListeners } from './ui.js';

// Wait until the entire HTML document is fully loaded and parsed
document.addEventListener('DOMContentLoaded', () => {
    // Only then, run the setup function to attach event listeners
    setupEventListeners();
});