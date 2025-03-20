LANGUAGES = ("en", "pl")

BABEL_DEFAULT_LOCALE = "en"

FILTERS_FOR = {
    "name": {"name": "div", "class_": "js_searchInGoogleTooltip breadcrumbs__item"},
    "score": {"name": "span", "class_": "product-review__score", "content": True},
    "review_count": {"name": "a", "class_": "product-review__link link link--accent js_reviews-link js_clickHash js_seoUrl"},
    "review_block": {"name": "div", "class_": "js_product-reviews js_reviews-hook js_product-reviews-container"},
    "review": {"name": "div", "class_": "user-post user-post__card js_product-review"},
    "next_location": {"name": "a", "class_": "pagination__item pagination__next", "href": True}
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
        "Cookie": "sv3=1.0_d8356090-05b5-11f0-b523-cf299fad1472; __RequestVerificationToken=NB-PZOYpaFQJ6cNWHLj5ZjloceFcXE1uekY92MlGRZOcqjMAxrS2x0oetsz0H8FJXVOAHbme74Fo91MQjpg6H4ISxvxDYBLwmF7aLwKZ3281; userCeneo=ID=d62564e3-6e46-4a20-8e8c-da145d71130f; ai_user=CT/5Y|2025-03-20T18:05:03.876Z; ai_session=tWg6E|1742493904121|1742493904121; __utmf=85c93a8bf24786ba1ec7792938a094ca_WRCdcwVynH5nQgti7pMQYQ%3D%3D; appType=%7B%22Value%22%3A1%7D; cProdCompare_v2=; browserBlStatus=0; ga4_ga=GA1.2.d8356090-05b5-11f0-b523-cf299fad1472; ga4_ga_K2N2M0CBQ6=GS1.2.1742493904.1.0.1742493906.0.0.533795806; _gcl_au=1.1.257172017.1742493906; FPID=FPID2.2.cr0XMjI9CXaq5MmIieYFoxuePIUJ78cNU1NM9J7c7iQ%3D; FPLC=7D1Df8rxmKAdDagzu%2BD01gHHrF1pTBkAN5Thjx2i2nXjURsilF4D6PE6tXMHff095T725KCWEZ3o3RFTIogrnX0%2F37G3YLANEi%2BfyM74iTzx7kI%3D; consentcookie=eyJBZ3JlZUFsbCI6dHJ1ZSwiQ29uc2VudHMiOlsxLDMsNCwyXSwiVENTdHJpbmciOiJDUU9rWWtBUU9rWWtBR3lBQkJQTEJoRXNBUF9nQUFBQUFCNVlJTnBEN0JiQkxVRkF3RmhqWUtzUU1JRVRVTUNBQW9RQUFBYUJBQ0FCUUFLUUlBUUNra0FRQkFTZ0JBQUNBQUFBSUNSQklRQU1BQUFBQ0VBQVFBQUFJQUFFQUFDUUJRQUlBQUFBZ0FBUUFBQVlBQUFpQUlBQUFBQUlnQUlBRUFBQW1RaEFBQUlBRUVBQWhBQUVJQUFBQUFBQUFBQUFBZ0FBQUFBQ0FBSUFBQUFBQUNBQUFJSU5nQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUJZS0FEQUFFRUd3a0FHQUFJSU5ob0FNQUFRUWJFUUFZQUFnZzJLZ0F3QUJCQnNaQUJnQUNDRFk2QURBQUVFR3lFQUdBQUlJTmtvQU1BQVFRYktRQVlBQWdnMldnQXdBQkJCc0EiLCJWZXJzaW9uIjoidjMifQ==",
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
