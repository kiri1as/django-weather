function weatherThemeErrorPage() {
    const weatherClasses = ['sunny', 'rainy', 'snowy', 'cloudy'];
    document.body.className = weatherClasses[Math.floor(Math.random() * weatherClasses.length)];
}

weatherThemeErrorPage();