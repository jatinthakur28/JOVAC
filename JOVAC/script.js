document.addEventListener('DOMContentLoaded', function() {
    const predictButton = document.getElementById('predictButton');
    const resultDiv = document.getElementById('result');
    const IP =document.getElementById("IP");

    predictButton.addEventListener('click', function() {
        const hours = parseFloat(IP.value);
        if (hours > 9.9 || hours < 0.1) {
            resultDiv.innerHTML = 'Limit breached';
            return;
        }

        fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json'
            },
            body: JSON.stringify({
            hours: hours,
            })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerText = `Prediction: ${parseInt(data.predicted_score, 10)}`;
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});