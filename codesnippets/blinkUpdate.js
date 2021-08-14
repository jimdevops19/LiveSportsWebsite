function blinkUpdate(element, newValue, newColor='#00ff00') {
    previousColor = element.style.color;
    element.innerHTML = newValue;
    element.style.color = newColor;
    // Set back to original color after timeout ms
    setTimeout(() => {
        element.style.color = previousColor
    }, 2000)
}
