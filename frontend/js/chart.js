let regressionChart; // A variable within the module to hold the chart instance

/**
 * Displays the analysis result on a canvas element.
 * @param {CanvasRenderingContext2D} ctx - The 2D context of the canvas element.
 * @param {Object} data - The analysis result data from the backend.
 */
export function displayChart(ctx, data) {
    // Destroy the old chart if it exists to prevent flickering
    if (regressionChart) {
        regressionChart.destroy();
    }

    const scatterData = data.original_data.map(p => ({ x: p[0], y: p[1] }));
    const lineData = data.regression_line;

    regressionChart = new Chart(ctx, {
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