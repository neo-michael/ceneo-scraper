const createTable = (tableId, data, columns) => {
    return new Tabulator(tableId, {
        data: data,
        layout: "fitColumns",
        addRowPos: "top",
        pagination: "local",
        paginationSize: 10,
        paginationCounter: "rows",
        movableColumns: true,
        columnDefaults: {
            tooltip: true,
        },
        columns: columns
    })
}
