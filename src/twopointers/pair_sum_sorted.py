from typing import List


def pair_sum_sorted(sorted: List[int], target: int) -> List[int]:
    left = 0
    right = len(sorted) - 1

    while left < right:
        res = sorted[left] + sorted[right]
        if res == target:
            return [left, right]
        elif res < target:
            left += 1
        else:
            right -= 1

    return []
