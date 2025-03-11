let toggle_loader = (show) => {
    const loader = document.getElementById('loader_overlay');
    const body = document.body;
    if (show) {
        loader.style.display = 'flex';
        body.classList.add('loading');
    } else {
        loader.style.display = 'none';
        body.classList.remove('loading');
    }
}

// HACK: disable loader when the page changes
setInterval(() => {
    if (window.performance.getEntriesByType("navigation")[0].type !== "navigate") {
        toggle_loader(false)
    }
}, 1000);