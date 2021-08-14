function updateElement(match) {
    Object.entries(match).forEach(([k,v]) => {
        element = document.getElementById('ELEMENT_ID');
        // Get Previous value first
        previousValue = element.innerHTML;

        // If Previous value is not equal to the new value, change it!
        if (previousValue !== v.toString()) {
            element.innerHTML = v.toString();
        }
    })
}