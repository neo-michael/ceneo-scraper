const toggleLoader = (show) => {
    const loader = document.getElementById("loader-overlay");

    if (show) {
        loader.style.display = "flex";
        document.body.classList.add("loading");
    } else {
        loader.style.display = "none";
        document.body.classList.remove("loading");
    }
}

// HACK: disable loader when the page is refreshed
setInterval(() => {
    if (window.performance.getEntriesByType("navigation")[0].type !== "navigate") {
        toggleLoader(false)
    }
}, 1000);