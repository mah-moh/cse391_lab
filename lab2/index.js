const qoutes = [
    'The greatest glory in living lies not in never falling, but in rising every time we fall.',
    'The way to get started is to quit talking and begin doing.',
    'Your time is limited, so don’t waste it living someone else’s life.',
    'If life were predictable it would cease to be life, and be without flavor.',
    'If you set your goals ridiculously high and it’s a failure, you will fail above everyone else’s success.',
    'Life is what happens when you’re busy making other plans.',
    'Spread love everywhere you go. Let no one ever come to you without leaving happier.',
    'When you reach the end of your rope, tie a knot in it and hang on.',
]

document.getElementById('random-qoute').innerHTML = qoutes[Math.floor(Math.random() * qoutes.length)]