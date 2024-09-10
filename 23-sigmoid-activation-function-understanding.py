import math
import numpy as np

def sigmoid(z: float) -> float:
    return np.round(1 / (1 + math.exp(-z)), 4)

if __name__ == '__main__':
    actual = sigmoid(0)
    expected = 0.5
    try:
        assert actual == expected
        print("Test passed!")
    except AssertionError as e:
        print("Test failed:", str(e))
