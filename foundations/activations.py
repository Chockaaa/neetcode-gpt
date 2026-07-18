import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        sigmoid_x = 1 / (1 + np.exp(-z))
        print(sigmoid_x)
        print(np.round(sigmoid_x,5))
        val = np.round(sigmoid_x,5)
        print(val)
        return val

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        print(z)
        for i in range(len(z)):
            print()
            z[i] = max(0,z[i])
        print(z)
        return z
