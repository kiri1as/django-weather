const weatherClasses = ['sunny', 'rainy', 'snowy', 'cloudy'];
const randomWeather = weatherClasses[Math.floor(Math.random() * weatherClasses.length)];
document.body.className = randomWeather;
