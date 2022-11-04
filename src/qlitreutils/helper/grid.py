"""
グリッド問題のヘルパー
"""


class Grid:
    """グリッドクラス"""

    def __init__(self, data: list):
        """
        :param data: 二次元リスト
        """
        self.data = data
        self.height = self.get_height()
        self.width = self.get_width()

    def get_height(self) -> int:
        return len(self.data)

    def get_width(self) -> int:
        return len(self.data[0])

    def look_top(self, row: int, col: int):
        """
        一つ上のマスを取得する
        """
        if row <= 0:
            return None
        else:
            return self.data[row - 1][col]

    def look_bottom(self, row: int, col: int):
        """
        一つ下のマスを取得する
        """
        if row >= self.height - 1:
            return None
        else:
            return self.data[row + 1][col]

    def look_left(self, row: int, col: int):
        """
        一つ左のマスを取得する
        """
        if col <= 0:
            return None
        else:
            return self.data[row][col - 1]

    def look_right(self, row: int, col: int):
        """
        一つ右のマスを取得する
        """
        if col >= self.width - 1:
            return None
        else:
            return self.data[row][col + 1]

    def look_through_top(self, row: int, col: int, obstacle=None) -> list:
        """
        障害物にぶつかるまで上のマスを取得する
        """
        ret = []
        if row == 0:
            return ret
        for i in range(1, row):
            row_pos = row - i
            item = self.data[row_pos][col]
            if obstacle and item == obstacle:
                break
            ret.append(item)
        return ret

    def look_through_bottom(self, row: int, col: int, obstacle=None) -> list:
        """
        障害物にぶつかるまで下のマスを取得する
        """
        ret = []
        if row == self.height - 1:
            return ret
        for row_pos in range(row + 1, self.height):
            item = self.data[row_pos][col]
            if obstacle and item == obstacle:
                break
            ret.append(item)
        return ret

    def look_through_right(self, row: int, col: int, obstacle=None) -> list:
        """
        障害物にぶつかるまで右のマスを取得する
        """
        ret = []
        if col == self.width - 1:
            return ret
        for col_pos in range(col + 1, self.width):
            item = self.data[row][col_pos]
            if obstacle and item == obstacle:
                break
            ret.append(item)
        return ret

    def look_through_left(self, row: int, col: int, obstacle=None) -> list:
        """
        障害物にぶつかるまで左のマスを取得する
        """
        ret = []
        if col == 0:
            return ret
        for i in range(1, col):
            col_pos = col - i
            item = self.data[row][col_pos]
            if obstacle and item == obstacle:
                break
            ret.append(item)
        return ret
