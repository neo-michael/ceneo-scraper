from flask import current_app

from .utils import escape_string

from ..models.review import Review

class ReviewParser:

    def parse(self, content):
        review = Review()

        review.id = content["data-entry-id"]
        review.author = self._parse_author(content)
        review.recommend = self._parse_recommend(content)
        review.stars = self._parse_stars(content)

        (
            review.published_datetime,
            review.purchase_datatime,
            review.updated_datetime,
        ) = self._parse_datetimes(content)

        review.likes = self._parse_rating(content, "yes", review.id)
        review.dislikes = self._parse_rating(content, "no", review.id)
        review.origin = self._parse_origin(content)
        review.text = self._parse_text(content)
        review.is_verified = self._parse_verified(content)
        review.images = self._parse_images(content)

        review.pros, review.cons = self._parse_pros_and_cons(content)

        return review

    def _parse_author(self, content):
        tag = content.find(**current_app.get_filter("author"))
        if not tag:
            return ""

        return escape_string(tag.text).strip()

    def _parse_recommend(self, content):
        tag = content.find(**current_app.get_filter("recommend"))
        if not tag:
            return False

        em_tag = tag.find("em")
        if not em_tag:
            return False

        if "recommended" in em_tag["class"]:
            return True

        return False

    def _parse_stars(self, content):
        tag = content.find(**current_app.get_filter("stars"))
        if not tag:
            return -1.0

        (score, total) = tag.text.strip().split("/")

        # Python expects float with dot as a decimal seperator
        score = score.replace(",", ".")

        return float(score)

    def _parse_datetimes(self, content):
        tag = content.find(**current_app.get_filter("dates"))
        if not tag:
            return ("", "", "")

        time_tag = tag.find_all("time")

        result = []

        for dt_tags in time_tag:
            result.append(dt_tags["datetime"])

        # Ensure the result has at least size 3
        while len(result) < 3:
            result.append("")

        return tuple(result)

    def _parse_rating(self, content, rating, id):
        tag_filter = current_app.get_filter("rating").copy()

        tag_filter["id"] = tag_filter["id"].format(rating = rating, id = id)

        tag = content.find(**tag_filter)
        if not tag:
            return 0

        return int(tag.text.strip())

    def _parse_origin(self, content):
        result = ""
        tag = content.find(**current_app.get_filter("origin"))
        if not tag:
            return result

        result += escape_string(tag.text)

        strong_tag = tag.find("strong")
        if not strong_tag:
            return result

        result += escape_string(strong_tag.text)

        return result.strip()

    def _parse_text(self, content):
        tag = content.find(**current_app.get_filter("text"))
        if not tag:
            return ""

        return escape_string(tag.text).strip()
    

    def _parse_verified(self, content):
        tag = content.find(**current_app.get_filter("verified"))
        if not tag:
            return False

        return True

    def _parse_images(self, content):
        result = []

        tag = content.find(**current_app.get_filter("images"))
        if not tag:
            return result

        div_tags = tag.find_all("div")

        for div in div_tags:
            link = div.find("a", href=True)
            if not link:
                continue

            result.append(link["href"])

        return result

    def _parse_pros_and_cons(self, content):
        tag = content.find(**current_app.get_filter("pros&cons"))
        if not tag:
            return ([], [])
        
        pros_tags = tag.find_all(**current_app.get_filter("pros"))
        cons_tags = tag.find_all(**current_app.get_filter("cons"))

        pros = self._parse_trait(pros_tags)
        cons = self._parse_trait(cons_tags)

        return (pros, cons)
                      
    def _parse_trait(self, tags):
        result = []
        for tag in tags:
            result.append(escape_string(tag.text).strip())
        return result
