from bisect import bisect_left
from collections import deque


def bubble_sort(a_list: list) -> list:
    """バブルソート"""
    loop_size = len(a_list) - 1
    for i in range(loop_size):
        no_swaps = True
        for j in range(loop_size - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
        if no_swaps:
            return a_list
    return a_list


def insertion_sort(a_list: list) -> list:
    """挿入ソート"""
    for i in range(1, len(a_list)):
        # 値を保持
        value = a_list[i]
        # 値が左の数字より小さくなるまで続ける
        while i > 0 and a_list[i - 1] > value:
            # 要素を右にずらしていく
            a_list[i] = a_list[i - 1]
            # カウントダウン
            i = i - 1
        # ループが終了したら正しい位置に挿入
        a_list[i] = value
    return a_list


def merge_sort(a_list: list) -> list:
    """マージソート"""
    if len(a_list) > 1:
        # 再帰的に分割
        mid = len(a_list) // 2
        left = a_list[:mid]
        right = a_list[mid:]

        merge_sort(left)
        merge_sort(right)
        # 二つのリストをマージ
        left_i = 0
        right_i = 0
        alist_i = 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] <= right[right_i]:
                a_list[alist_i] = left[left_i]
                left_i += 1
            else:
                a_list[left_i] = right[right_i]
                right_i += 1
            alist_i += 1

        while left_i < len(left):
            a_list[alist_i] = left[left_i]
            left_i += 1
            alist_i += 1

        while right_i < len(right):
            a_list[alist_i] = right[right_i]
            right_i += 1
            alist_i += 1
    return a_list


def get_before_in_sorted_permutation(a_list: list) -> list:
    """順列で並び替えた際の一つ前の配列を返す"""
    ret = []
    tmp = deque()

    first = True
    min_val = 0
    for i, val in enumerate(reversed(a_list)):
        if first:
            min_val = val
            tmp.appendleft(val)
            first = False
            continue
        if val <= min_val:
            min_val = val
            tmp.appendleft(val)
        else:
            tmp = list(tmp)
            sorted_tmp = sorted(tmp)
            index = bisect_left(sorted_tmp, val) - 1
            changed_val = sorted_tmp[index]
            change_index = tmp.index(changed_val)
            tmp[change_index] = val
            tmp.sort(reverse=True)
            tmp = [changed_val] + tmp
            remain = len(a_list) - 1 - i
            ret = a_list[:remain] + tmp
            break

    if not ret:
        return a_list
    else:
        return ret


def get_after_in_sorted_permutation(a_list: list) -> list:
    """順列で並び替えた際の一つ後ろの配列を返す"""
    ret = []
    tmp = deque()

    first = True
    max_val = 0
    for i, val in enumerate(reversed(a_list)):
        if first:
            max_val = val
            tmp.appendleft(val)
            first = False
            continue
        if val >= max_val:
            max_val = val
            tmp.appendleft(val)
        else:
            tmp = list(tmp)
            sorted_tmp = sorted(tmp)
            index = bisect_left(sorted_tmp, val)
            changed_val = sorted_tmp[index]
            change_index = tmp.index(changed_val)
            tmp[change_index] = val
            tmp.sort()
            tmp = [changed_val] + tmp
            remain = len(a_list) - 1 - i
            ret = a_list[:remain] + tmp
            break

    if not ret:
        return a_list
    else:
        return ret
