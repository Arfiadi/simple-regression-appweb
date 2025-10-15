let regressionChart; // Variabel global di dalam modul untuk menyimpan objek grafik

/**
 * Menampilkan hasil analisis pada sebuah elemen canvas.
 * @param {HTMLCanvasElement} canvasElement - Elemen canvas untuk menggambar.
 * @param {Object} data - Data hasil analisis dari backend.
 */
export function displayChart(canvasElement, data) {
    // Hancurkan grafik lama jika ada untuk mencegah tumpang tindih
    if (regressionChart) {
        regressionChart.destroy();
    }

    const scatterData = data.original_data.map(p => ({ x: p[0], y: p[1] }));
    const lineData = data.regression_line;

    regressionChart = new Chart(canvasElement, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Original Data',
                data: scatterData,
                backgroundColor: 'rgba(0, 123, 255, 0.6)',
            }, {
                label: 'Regression Line',
                data: lineData,
                type: 'line',
                borderColor: 'rgba(220, 53, 69, 1)',
                backgroundColor: 'transparent',
                borderWidth: 2,
                pointRadius: 0,
                fill: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    title: { display: true, text: 'Independent Variable (X)', font: { size: 14 } }
                },
                y: {
                    title: { display: true, text: 'Dependent Variable (Y)', font: { size: 14 } }
                }
            }
        }
    });
}