class Review:
    def __init__(self):
        self.id = ""
        self.author = ""
        self.recomend = False
        # self.is_ai_highlight = False
        self.stars = 1.0
        self.published_datetime = ""
        self.purchase_datatime = ""
        self.updated_datetime = ""
        self.likes = 0
        self.dislikes = 0
        self.origin = ""
        self.text = ""
        self.is_verified = False
        self.images = []
        self.pros = []
        self.cons = []
        self.comments = []


# author name: str
# recomend: bool
# stars: float [1-5]
# date published: str
# time used before listing: str
# likes: int
# dislikes: int
# review origin: str
# review content: str
# is verified: bool
# images: list[str] - links to images on ceneo.pl
# comments: list[Comment]
