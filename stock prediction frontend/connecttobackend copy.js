document.getElementById('stock-form').addEventListener('submit', async function (e) {
    e.preventDefault(); // Prevent form refresh

    // Get user inputs
    const stock = document.getElementById('stock-dropdown').value;
    const timeframe = document.getElementById('timeframe').value;
    const spinner = document.getElementById('loading-container'); // Spinner container
    const resultSection = document.getElementById('results-section'); // Results section
    const resultMessage = document.getElementById('result'); // Result message container

    // Validate inputs
    if (!stock || !timeframe) {
        alert("Please select both a stock and a timeframe.");
        return;
    }

    // Format stock symbol for backend compatibility (add `.NS` if missing)
    const formattedStock = stock.includes('.NS') ? stock : `${stock}.NS`;

    // Show spinner and hide results during request
    spinner.style.display = 'block';
    resultSection.style.display = 'none';

    try {
        // Log the request payload for debugging
        console.log("Submitting request to backend with payload:", { stock: formattedStock, timeframe });

        // Make POST request to backend
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ stock: formattedStock, timeframe }),
        });

        // Log the raw response object
        console.log("Response received:", response);

        // Check if response is okay
        if (!response.ok) {
            throw new Error(`Backend error: ${response.status} ${response.statusText}`);
        }

        // Parse JSON response
        const data = await response.json();
        console.log("Parsed response data:", data); // Debugging: Log parsed response

        // Check for backend errors in the response
        if (data.error) {
            throw new Error(data.error);
        }

        // Hide spinner and display the results section
        spinner.style.display = 'none';
        resultSection.style.display = 'block';
        console.log("Result section visibility:", resultSection.style.display); // Log visibility

        // Display prediction results
        resultMessage.innerHTML = `
        <strong>Predicted Price:</strong> ${data.predicted_price.toFixed(2)}<br>
        <strong>Percentage Change:</strong> ${data.percentage_change.toFixed(2)}%
        `;
        console.log("Result message content:", resultMessage.innerHTML); // Log result content

        // Render chart with data
        renderChart(data.dates, data.historical_prices, data.predicted_prices);

    } catch (error) {
        // Log the error
        console.error("Error occurred:", error);

        // Hide spinner and display error message
        spinner.style.display = 'none';
        resultSection.style.display = 'block';
        resultMessage.innerText = `Error: ${error.message}`;
        resultMessage.classList.replace('alert-info', 'alert-danger');
    }
});

// Render Chart Function
function renderChart(dates, historicalPrices, predictedPrices) {
    const ctx = document.getElementById('results-chart').getContext('2d');

    // Destroy any existing chart before creating a new one
    if (window.myChart) {
        window.myChart.destroy();
    }

    // Create the chart
    window.myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [
                {
                    label: 'Smoothed Historical Prices',
                    data: historicalPrices,
                    borderColor: 'blue',
                    borderWidth: 1,
                },
                {
                    label: 'Predicted Prices',
                    data: predictedPrices,
                    borderColor: 'red',
                    borderWidth: 1,
                    borderDash: [5, 5],
                },
            ],
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: 'Date' } },
                y: { title: { display: true, text: 'Price' } },
            },
        },
    });
    console.log("Chart rendered successfully."); // Debugging: Log after chart rendering
}


