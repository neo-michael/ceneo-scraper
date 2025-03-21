const textFormatter = (cell, max = 50) => {
    const fullText = cell.getValue() || ""
    const shortText = fullText.length > max ? fullText.substring(0, max) + "…" : fullText

    return `
    <div class="text-wrapper short">
        ${shortText}
    </div>
    <div class="text-wrapper full">
        ${fullText}
    </div>
    `
}

const textCellClickHandler = (e, cell) => {
    const el = cell.getElement()
    const shortEl = el.querySelector('.text-wrapper.short')
    const fullEl = el.querySelector('.text-wrapper.full')

    const isExpanded = window.getComputedStyle(fullEl).display !== "none"
    if (isExpanded) {
        shortEl.style.display = "block"
        fullEl.style.display = "none"

        cell.getRow().normalizeHeight()
    } else {
        shortEl.style.display = "none"
        fullEl.style.display = "block"

        cell.getRow().normalizeHeight()

        const rowEl = cell.getRow().getElement()
        rowEl.scrollIntoView({ behavior: "smooth", block: "nearest" })
    }

    e.stopPropagation();
}

const titleFormatter = (cell) => {
    const rowData = cell.getData()
    const id = rowData["id"]
    const name = cell.getValue()
    return `<a href="https://ceneo.pl/${id}" target="_blank">${name}</a>`
}