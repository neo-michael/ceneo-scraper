import json

class Review:
    def __init__(self):
        self.id = ""
        self.author = ""
        self.recommend = False
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

    def to_json_str(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)

