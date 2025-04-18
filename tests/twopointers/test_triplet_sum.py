from src.twopointers.triplet_sum import triplet_sum


def test_triplet_sum():
    # assert triplet_sum([0, -1, 2, -3, 1]) == [[-3, 1, 2], [-1, 0, 1]]
    # assert triplet_sum([]) == []
    # assert triplet_sum([0]) == []
    # assert triplet_sum([1, -1]) == []
    # assert triplet_sum([0, 0, 0]) == [[0, 0, 0]]
    # assert triplet_sum([1, 0, 1]) == []
    assert triplet_sum([0, 0, 1, -1, 1, -1]) == [[-1, 0, 1]]
