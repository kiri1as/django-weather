function applyRandomGradientTheme() {
    const WEATHER_GRADIENTS = [
        {
            background: 'linear-gradient(to right, #87CEEB, #00BFFF)', // Clear sky
            color: '#000'
        },
        {
            background: 'linear-gradient(to right, #778899, #2F4F4F)', // Cloudy
            color: '#fff'
        },
        {
            background: 'linear-gradient(to right, #4682B4, #1E90FF)', // Rainy
            color: '#fff'
        },
        {
            background: 'linear-gradient(to right, #FFD700, #FFA500)', // Sunny
            color: '#000'
        },
        {
            background: 'linear-gradient(to right, #708090, #2C3E50)', // Stormy
            color: '#fff'
        }
    ]

    const app = document.getElementById('app');
    let rnd = Math.random() * WEATHER_GRADIENTS.length;
    const randomGradient = WEATHER_GRADIENTS[Math.floor(rnd)];
    const buttons = document.getElementsByClassName('action-button');

    app.style.background = randomGradient.background;
    app.style.color = randomGradient.color;

    buttons.forEach(button => {
        const backgroundColor = randomGradient.color;
        button.style.backgroundColor = backgroundColor;

        if (backgroundColor === '#000') {
            button.style.color = '#fff'
        }
    })
}

applyRandomGradientTheme();