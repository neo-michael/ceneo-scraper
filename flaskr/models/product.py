import json

class Product():
    def __init__(self):
        self.id = ""
        self.name = ""
        self.review_count = 0
        self.avg_score = 0.0
        self.pros_count = 0
        self.cons_count = 0
        self.csv = ""
        self.json = ""
        self.xlsx = ""
    
    def to_json_str(self):
        return json.dumps(self, default=lambda o: o.__dict__, ensure_ascii=False)
