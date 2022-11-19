"""
二次元平面問題のヘルパー
"""
import itertools
import math
from math import cos, sin


def is_three_points_on_same_line(x1, y1, x2, y2, x3, y3) -> bool:
    """平面座標上の三点が同一直線にあるか判定する"""
    return (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1)


def get_length_between_two_points(point1: tuple, point2: tuple) -> float:
    """2点間の距離を返す"""
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    if x1 == x2:
        return abs(y2 - y1)
    if y1 == y2:
        return abs(x2 - x1)

    x_length = abs(x2 - x1)
    y_length = abs(y2 - y1)
    tmp = x_length ** 2 + y_length ** 2
    return pow(tmp, 0.5)


def check_square_by_line(point1: tuple, point2: tuple, point3: tuple, point4: tuple) -> bool:
    """4点が正方形を構成しているか判定する"""
    pairs = itertools.combinations([point1, point2, point3, point4], 2)
    lines = []
    for pair in pairs:
        lines.append(get_length_between_two_points(pair[0], pair[1]))
    lines.sort()
    l1, l2, l3, l4 = lines[:4]
    l5, l6 = lines[4:]
    if l1 == l2 == l3 == l4:
        if l5 == l6:
            # todo:そのままやるとイコールにならないので、intで無理やり併せている。たぶん正確ではない。
            if int(l5 ** 2) == int(2 * (l1 ** 2)):
                return True
    return False


def get_square_point(point1: tuple, point2: tuple):
    """
    ４点の座標が正方形を作っているときに、２点の座標から残り２点の座標を特定する
    point1はpoint2の左上にある場合を要件とする
    """
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    # 左にない場合
    if x1 >= x2:
        raise ValueError('point１は左上の点を指定してください')
    # 上にない場合
    if y1 <= y2:
        raise ValueError('point１は左上の点を指定してください')
    dx = x2 - x1
    dy = y1 - y2

    # 差から座標を特定
    x3 = x2 - dy
    x4 = x3 - dx
    y3 = y2 - dx
    y4 = y3 + dy
    return (x3, y3), (x4, y4)


def get_center_point(point1: tuple, point2: tuple) -> tuple:
    """2点の中心点を返す"""
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    return tuple([cx, cy])


def get_rotate_point(point: tuple, degree: float):
    """
    (x,y)  を原点中心に反時計回りに θ 回転させた点の座標を返す
    """
    x, y = point[0], point[1]
    radian = math.radians(degree)
    x1 = cos(radian) * x - sin(radian) * y
    y1 = sin(radian) * x + cos(radian) * y
    return tuple([x1, y1])


def get_max_manhattan_distance(points: list) -> int:
    """
    座標リストを受け取り最大のマンハッタン距離を返す
    """
    x_conv = []
    y_conv = []

    for x, y in points:
        x_conv.append(x + y)
        y_conv.append(x - y)
    x_dist_max = abs(max(x_conv) - min(x_conv))
    y_dist_max = abs(max(y_conv) - min(y_conv))

    return max(x_dist_max, y_dist_max)
