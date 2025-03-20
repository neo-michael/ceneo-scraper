const dismissError = () => {
    const errorBox = document.getElementById("error-container");

    if (!errorBox) {
        return
    }
    
    errorBox.style.display = "none";
}