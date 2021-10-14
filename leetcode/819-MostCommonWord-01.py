import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        words = re.split('[^a-z]+', paragraph)
        resultwords = [word for word in words if word not in banned]
        most_common_item = max(resultwords, key=resultwords.count)
        return most_common_item
