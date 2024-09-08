import numpy as np
import numpy.typing as npt

def rref(matrix: npt.ArrayLike) -> npt.ArrayLike:
    res = np.array([])

    

    return res

if __name__ == '__main__':
    mat = np.array([
        [1, 2, -1, -4],
        [2, 3, -1, -11],
        [-2, 0, -3, 22]
    ])

    rref_matrix = rref(mat)

    expected = np.array([
        [ 1,  0,  0, -8,],
        [ 0,  1,  0,  1,],
        [-0, -0,  1, -2,]
    ])
    try:
        np.testing.assert_array_equal(rref_matrix, expected)
        print('Test passed!')
    except AssertionError as e:
        print('Test failed:', str(e))
