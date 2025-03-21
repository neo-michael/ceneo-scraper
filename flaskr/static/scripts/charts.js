const createChartData = (labels, data, chartSettings) => {
    return {
        labels: labels,
        datasets: [{
            data: data,
            ...chartSettings
        }]
    }
}

const createChart = (chartId, type, chartData, tooltipCallback, scales={}, legend={}) => {
    const context = document.getElementById(chartId).getContext("2d")

    return new Chart(context, {
        type: type,
        data: chartData,
        options: {
            responsive: true,
            scales: scales,
            plugins: {
                legend: legend,
                tooltip: {
                    callbacks: {
                        label: tooltipCallback
                    }
                }
            }
        }
    })
}