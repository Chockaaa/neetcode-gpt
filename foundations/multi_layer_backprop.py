import numpy as np
from typing import List



class Solution:
    def relu(self,x):
        return np.maximum(0, x)

    def forward_and_backward(self,
                              x: List[float],
                              W1: List[List[float]], b1: List[float],
                              W2: List[List[float]], b2: List[float],
                              y_true: List[float]) -> dict:
        # Architecture: x -> Linear(W1, b1) -> ReLU -> Linear(W2, b2) -> predictions
        # Loss: MSE = mean((predictions - y_true)^2)
        #
        # Return dict with keys:
        #   'loss':  float (MSE loss, rounded to 4 decimals)
        #   'dW1':   2D list (gradient w.r.t. W1, rounded to 4 decimals)
        #   'db1':   1D list (gradient w.r.t. b1, rounded to 4 decimals)
        #   'dW2':   2D list (gradient w.r.t. W2, rounded to 4 decimals)
        #   'db2':   1D list (gradient w.r.t. b2, rounded to 4 decimals)

        values = {}

        z1 = np.dot(W1,x) + b1
        a1 = self.relu(z1)
        z2 = np.dot(W2,a1) + b2
        
        loss = np.mean((z2-y_true)**2)
        values['loss'] = np.round(loss,4)

        dl_dz2 = 2 * (z2 - y_true)/ len(y_true)
        dl_dw2 = np.outer(dl_dz2,a1)
        values['dW2'] = np.round(dl_dw2,4)

        dl_db2 = dl_dz2
        values['db2'] = np.round(dl_db2,4)

        dl_da1 = np.array(W2).T @ dl_dz2
        dl_dz1 = dl_da1 * (z1 > 0)

        dl_dw1 = np.outer(dl_dz1,x)
        values['dW1'] = np.round(dl_dw1,4)

        dl_db1 = dl_dz1
        values['db1'] = np.round(dl_db1,4)

        print(values)
        return values
