import numpy as np
import numpy.typing as npt


def rref(A: npt.ArrayLike) -> npt.ArrayLike:
    # pylint: disable-next=consider-using-enumerate
    for i in range(len(A)):
        if A[i, i] == 0:
            nonzero_rel_locs = A[i:, i].nonzero()[0]
            if len(nonzero_rel_locs) == 0:
                continue
            A[i] += A[nonzero_rel_locs[0] + i]

        A[i] = A[i] / A[i, i]
        # pylint: disable-next=consider-using-enumerate
        for j in range(len(A)):
            if i == j:
                continue

            A[j] -= A[j, i] * A[i]

    return A


if __name__ == "__main__":
    mat = np.array([[1, 2, -1, -4], [2, 3, -1, -11], [-2, 0, -3, 22]])

    rref_matrix = rref(mat)
    expected = np.array([
        [ 1, 0, 0, -8, ],
        [ 0, 1, 0, 1, ],
        [ -0, -0, 1, -2, ],
    ])
    try:
        np.testing.assert_array_equal(rref_matrix, expected)
        print("Test passed!")
    except AssertionError as e:
        print("Test failed:", str(e))
