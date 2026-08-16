import numpy as np
from typing import List


class Solution:
    def rms_norm(self, x: List[float], gamma: List[float], eps: float) -> List[float]:
        # Implement RMS Normalization (similar to LayerNorm but without mean centering or beta)
        # Normalize x, then scale by gamma
        # Return result rounded to 4 decimal places as a list
        x = np.array(x, dtype=float)
        rms = np.sqrt(np.mean((np.square(x))+eps))
        gamma = np.array(gamma, dtype=float)


        x_val = x/rms * gamma

        return np.round(x_val,4)
