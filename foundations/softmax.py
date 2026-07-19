import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        exponential_score = []
        output_score = []
        max_z= max(z)

        for i in z:
            # print(i,math.exp(i))
            exponential_score.append(math.exp(i-max_z))
        
        # print(sum(exponential_score))
        total = sum(exponential_score)
        for i in exponential_score:
            # print(i/total)
            output_score.append(i/total)
        
        # print(np.round(output_score,4))

        return np.round(output_score,4)
