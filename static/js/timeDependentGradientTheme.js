function getRandomWeather() {
    const weatherConditions = ['clear', 'clouds', 'rain', 'snow', 'thunderstorm'];
    return weatherConditions[Math.floor(Math.random() * weatherConditions.length)];
}

function applyWeatherGradient() {
    const now = new Date();
    const hours = now.getHours();
    const weather = getRandomWeather();
    let gradient = '';


    if (weather === 'clear') {
        gradient = hours > 18 || hours < 6
            ? 'linear-gradient(to bottom, #2c3e50, #34495e)' // Ночь
            : 'linear-gradient(to bottom, #f39c12, #f1c40f)'; // День
    } else if (weather === 'clouds') {
        gradient = 'linear-gradient(to bottom, #bdc3c7, #2c3e50)';
    } else if (weather === 'rain') {
        gradient = 'linear-gradient(to bottom, #2980b9, #2c3e50)';
    } else if (weather === 'snow') {
        gradient = 'linear-gradient(to bottom, #ecf0f1, #95a5a6)';
    } else if (weather === 'thunderstorm') {
        gradient = 'linear-gradient(to bottom, #2c3e50, #8e44ad)';
    } else {
        gradient = 'linear-gradient(to bottom, #95a5a6, #7f8c8d)'; // По умолчанию
    }

    document.body.style.background = gradient;
}

applyWeatherGradient();