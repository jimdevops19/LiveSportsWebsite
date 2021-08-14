setInterval(function() {
    fetch("/info_json")
        .then(response => response.json())
        .then(data =>
            data.forEach(match=>
                updateElement(match)
            )
        );
}, 1000);

function updateElement(match) {
    Object.entries(match).forEach(([k,v]) => {
        element = document.getElementById(k + '_' + match.id.toString());
        // Previous value
        previousValue = element.innerHTML;
        if (previousValue !== v.toString() && k.toString() !== 'minute') {
            blinkUpdate(element, v.toString())
        }
        if (previousValue !== v.toString() && k.toString() === 'minute') {
            element.innerHTML = v.toString()
        }
    })
}

function blinkUpdate(element, newValue, newColor='#00ff00') {
    previousColor = element.style.color;
    element.innerHTML = newValue;
    element.style.color = newColor;
    // Set back to original color after timeout ms
    setTimeout(() => {
        element.style.color = previousColor
    }, 3000)
}

