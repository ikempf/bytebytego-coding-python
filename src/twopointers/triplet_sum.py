from typing import List


def triplet_sum(nums: List[int]) -> List[List[int]]:
    sorted = nums[:]
    sorted.sort()
    triplets = []

    print(sorted)
    for i, n in enumerate(sorted):
        if i > 0 and sorted[i] == sorted[i - 1]:
            continue
        pairs = _pair_sum(sorted[i + 1:], -n)
        print("======", i, pairs)
        for pair in pairs:
            triplet = pair + [n]
            triplet.sort()
            triplets.append(triplet)

    return triplets


def _pair_sum(sorted: List[int], target: int) -> List[List[int]]:
    left = 0
    right = len(sorted) - 1
    pairs = []

    while left < right:
        sum = sorted[left] + sorted[right]
        if sum == target:
            pairs.append([sorted[left], sorted[right]])
            left += 1
            while left < right and sorted[left] == sorted[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1

    return pairs
