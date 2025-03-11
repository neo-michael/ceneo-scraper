from .review import Review

class ReviewParser:

    def parse(self, content):
        review = Review()

        review.id = content["data-entry-id"]
        review.author = self._parse_author(content)
        review.recomend = self._parse_recomend(content)
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

        return review

    def _parse_author(self, content):
        tag = content.find("span", class_="user-post__author-name")
        if not tag:
            return ""

        return tag.text.strip()

    def _parse_recomend(self, content):
        tag = content.find("span", class_="user-post__author-recomendation")
        if not tag:
            return False

        recomend_tag = tag.find("em")
        if not recomend_tag:
            return False

        if "recommended" in recomend_tag["class"]:
            return True

        return False

    def _parse_stars(self, content):
        tag = content.find("span", class_="user-post__score-count")
        if not tag:
            return -1.0

        (score, total) = tag.text.strip().split("/")

        # Python won't parse floats with ','
        score = score.replace(",", ".")

        return float(score)

    def _parse_datetimes(self, content):
        tag = content.find("span", class_="user-post__published")
        if not tag:
            return ("", "", "")

        datetime_tags = tag.find_all("time")

        result = []

        for dt_tags in datetime_tags:
            result.append(dt_tags["datetime"])

        # Ensure the result has at least size 3
        while len(result) < 3:
            result.append("")

        return tuple(result)

    def _parse_rating(self, content, rating, id):
        tag = content.find("span", id=f"votes-{rating}-{id}")
        if not tag:
            return 0

        return int(tag.text.strip())

    def _parse_origin(self, content):
        result = ""
        tag = content.find("div", class_="user-post__origin")
        if not tag:
            return result

        result += tag.text

        strong_tag = tag.find("strong")
        if not strong_tag:
            return result

        result += strong_tag.text

        return result.strip()

    def _parse_text(self, content):
        tag = content.find("div", class_="user-post__text")
        if not tag:
            return ""

        return tag.text.strip()

    def _parse_verified(self, content):
        tag = content.find("div", class_="review-pz")
        if not tag:
            return False

        return True

    def _parse_images(self, content):
        result = []

        tag = content.find("div", class_="review-pictures js_product-review-carousel")
        if not tag:
            return result

        div_tags = tag.find_all("div")

        for div in div_tags:
            link = div.find("a", href=True)
            if not link:
                continue

            result.append(link["href"])

        return result
