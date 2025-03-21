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

// HACK: disable loader when the page changes
setInterval(() => {
    if (!window.location.href.includes("extract")) {
        toggleLoader(false)
    }
}, 500);