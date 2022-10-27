"""
グリッド問題のヘルパー
"""

from typing import List


class Grid:
    """グリッドクラス"""

    def __init__(self, data: List[List]):
        self.data = data
        self.height = self.get_height()
        self.width = self.get_width()

    def get_height(self) -> int:
        return len(self.data)

    def get_width(self) -> int:
        return len(self.data[0])

    def look_top(self, row: int, col: int):
        if row <= 0:
            return None
        else:
            return self.data[row - 1][col]

    def look_bottom(self, row: int, col: int):
        if row >= self.height - 1:
            return None
        else:
            return self.data[row + 1][col]

    def look_left(self, row: int, col: int):
        if col <= 0:
            return None
        else:
            return self.data[row][col - 1]

    def look_right(self, row: int, col: int):
        if col >= self.width - 1:
            return None
        else:
            return self.data[row][col + 1]
