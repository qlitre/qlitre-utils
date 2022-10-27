"""
二次元平面問題のヘルパー
"""


def is_three_points_on_same_line(x1, y1, x2, y2, x3, y3) -> bool:
    """平面座標上の三点が同一直線にあるか判定する"""
    return (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1)
