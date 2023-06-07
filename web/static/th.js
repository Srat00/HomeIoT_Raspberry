//function getData() {
//    // '/api/sensor-data' endpoint에서 데이터를 받아옵니다.
//    // 이 부분은 실제 MongoDB에서 데이터를 가져오도록 수정해야 합니다.
//    return fetch('/api/sensor-data')
//        .then(response => response.json());
//}

//document.addEventListener("DOMContentLoaded", () => {
//    function updateChart() {
//        getData().then((data) => {
//            const trace1 = {
//                x: data.map(d => new Date(d.createdAt)),
//                y: data.map(d => d.temperature),
//                mode: 'lines+markers',
//                type: 'scatter',
//                name: '온도',
//            };
//
//            const trace2 = {
//                x: data.map(d => new Date(d.createdAt)),
//                y: data.map(d => d.humidity),
//                mode: 'lines+markers',
//                type: 'scatter',
//                name: '습도',
//            };
//
//            const layout = {
//                title: '온도와 습도',
//                xaxis: { title: '시간' },
//                yaxis: { title: '값' },
//            };
//
//            Plotly.newPlot('chart', [trace1, trace2], layout);
//            setTimeout(updateChart, 1000 * 60 * 5); // 5분마다 업데이트
//        });
//    }
//
//    updateChart();
//});


function getDummyData() {
    const data = [];
    const now = Date.now();

    for (let i = 0; i < 24; i++) {
        data.push({
            createdAt: new Date(now - i * 60 * 60 * 1000),
            temperature: Math.random() * 10 + 20,
            humidity: Math.random() * 10 + 60,
        });
    }

    return data.reverse();
}

document.addEventListener("DOMContentLoaded", () => {
    function updateChart() {
        const data = getDummyData();
        const trace1 = {
            x: data.map(d => d.createdAt),
            y: data.map(d => d.temperature),
            mode: 'lines+markers',
            type: 'scatter',
            name: '온도',
        };

        const trace2 = {
            x: data.map(d => d.createdAt),
            y: data.map(d => d.humidity),
            mode: 'lines+markers',
            type: 'scatter',
            name: '습도',
        };

        const layout = {
            title: '온도와 습도',
            xaxis: { title: '시간' },
            yaxis: { title: '값' },
        };

        Plotly.newPlot('chart', [trace1, trace2], layout);
    }

    updateChart();
});

