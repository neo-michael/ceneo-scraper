const createTable = (tableId, data, columns, localization) => {
    return new Tabulator(tableId, {
        data: data,
        layout: "fitColumns",
        addRowPos: "top",
        pagination: "local",
        paginationSize: 15,
        paginationCounter: "rows",
        movableColumns: true,
        columnDefaults: {
            tooltip: true,
        },
        columns: columns,
        locale: true,
        langs: {
            "en-us": {
                "pagination": localization
            }
        }
    })
}
