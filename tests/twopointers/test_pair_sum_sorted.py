from src.twopointers.pair_sum_sorted import pair_sum_sorted


def test_pair_sum_sorted():
    assert pair_sum_sorted([-5, -2, 3, 4, 6], 7) == [2, 3]
    assert pair_sum_sorted([], 0) == []
    assert pair_sum_sorted([1], 1) == []
    assert pair_sum_sorted([2, 3], 5) == [0, 1]
    assert pair_sum_sorted([2, 2, 3], 5) == [0, 2]
    assert pair_sum_sorted([-1, 2, 3], 2) == [0, 2]
    assert pair_sum_sorted([-3, -2, -1], -5) == [0, 1]
