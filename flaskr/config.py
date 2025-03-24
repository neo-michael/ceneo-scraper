LANGUAGES = ("en", "pl")

BABEL_DEFAULT_LOCALE = "en"

FILTERS_FOR = {
    "name": {"name": "div", "class_": "js_searchInGoogleTooltip breadcrumbs__item"},
    "score": {"name": "span", "class_": "product-review__score", "content": True},
    "review_count": {
        "name": "a",
        "class_": "product-review__link link link--accent js_reviews-link js_clickHash js_seoUrl",
    },
    "review_block": {
        "name": "div",
        "class_": "js_product-reviews js_reviews-hook js_product-reviews-container",
    },
    "review": {"name": "div", "class_": "user-post user-post__card js_product-review"},
    "next_location": {
        "name": "a",
        "class_": "pagination__item pagination__next",
        "href": True,
    },
    "author": {"name": "span", "class_": "user-post__author-name"},
    "recommend": {"name": "span", "class_": "user-post__author-recomendation"},
    "stars": {"name": "span", "class_": "user-post__score-count"},
    "dates": {"name": "span", "class_": "user-post__published"},
    "rating": {"name": "span", "id": "votes-{rating}-{id}"},
    "origin": {"name": "div", "class_": "user-post__origin"},
    "text": {"name": "div", "class_": "user-post__text"},
    "verified": {"name": "div", "class_": "review-pz"},
    "images": {"name": "div", "class_": "review-pictures js_product-review-carousel"},
    "pros&cons": {"name": "div", "class_": "review-feature"},
    "pros": {"name": "div", "class_": "review-feature__item review-feature__item--positive"},
    "cons": {"name": "div", "class_": "review-feature__item review-feature__item--negative"},
}

HTTP_CONFIG = {
    "http2": True,
    "follow_redirects": True,
    # headers copy pasted from browser
    "headers": {
        "Host": "www.ceneo.pl",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Cookie": "sv3=1.0_38b22d77-088b-11f0-8921-3084f2169e1e; urdsc=1; userCeneo=ID=17296499-c41f-4dc3-bb12-1539ab412c5c; __RequestVerificationToken=KN0afpWJZoEFgDkrQhwF65Q8lp6cSVsJ0XMXVzfF7wkR0_9uTfsI4ZeridIhuHolgSTnkSdHMXT2hobNm4TBAB7fnVCNzVH_7MrvL2-kgVE1; ai_user=AQUld|2025-03-24T08:37:30.619Z; ai_session=L42LL|1742805451157|1742805451157; __utmf=b414cb999395ce25580bb106dbc2ba34_vqxRifw1T7TSnQ0XQcGl7g%3D%3D; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; ga4_ga=GA1.2.38b22d77-088b-11f0-8921-3084f2169e1e; ga4_ga_K2N2M0CBQ6=GS1.2.1742805450.1.0.1742805453.0.0.458134472; _gcl_au=1.1.132487356.1742805453; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUU94a1VBUU94a1VBR3lBQkJQTEJoRXNBUF9nQUFBQUFCNVlJTnBEN0JiQkxVRkF3RmhqWUtzUU1JRVRVTUNBQW9RQUFBYUJBQ0FCUUFLUUlBUUNra0FRQkFTZ0JBQUNBQUFBSUNSQklRQU1BQUFBQ0VBQVFBQUFJQUFFQUFDUUJRQUlBQUFBZ0FBUUFBQVlBQUFpQUlBQUFBQUlnQUlBRUFBQW1RaEFBQUlBRUVBQWhBQUVJQUFBQUFBQUFBQUFBZ0FBQUFBQ0FBSUFBQUFBQUNBQUFJSU5nQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRUd3a0FHQUFJSU5ob0FNQUFRUWJFUUFZQUFnZzJLZ0F3QUJCQnNaQUJnQUNDRFk2QURBQUVFR3lFQUdBQUlJTmtvQU1BQVFRYktRQVlBQWdnMldnQXdBQkJCc0EiLCJWZXJzaW9uIjoidjMifQ==; FPID=FPID2.2.rN6mlc12Gf%2BlvjaNw8HHqT9lX61U6JE5mPpMn53RxyU%3D; FPLC=yHtO6r04HJ%2FBqtuYsbr2kTLocA0eLvtK1CedkiiAcFU5xJIC8Esrqb8T8ev%2BAIimNy6G3%2FZ9BObf9BVL6RkGYf3W96TJM1qSWsnJHg03kZVPrr8%3D",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Priority": "u=0, i",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers",
    },
}
