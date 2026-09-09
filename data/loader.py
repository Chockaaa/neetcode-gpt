import torch
from torchtyping import TensorType
from typing import Tuple

class Solution:
    def create_batches(self, data: TensorType[int], context_length: int, batch_size: int) -> Tuple[TensorType[int], TensorType[int]]:
        # data: 1D tensor of encoded text (integer token IDs)
        # context_length: number of tokens in each training example
        # batch_size: number of examples per batch
        #
        # Return (X, Y) where:
        # - X has shape (batch_size, context_length)
        # - Y has shape (batch_size, context_length)
        # - Y is X shifted right by 1 (Y[i][j] = data[start_i + j + 1])
        #
        # Use torch.manual_seed(0) before generating random start indices
        # Use torch.randint to pick random starting positions
        X = []
        Y = []
        torch.manual_seed(0)
        start = torch.randint(0,len(data)-context_length,(batch_size,))
        X = []
        Y = []
        for i in range(len(start)):
            X.append(data[start[i] : start[i] + context_length].tolist())
            Y.append(data[start[i] + 1 : start[i] + 1 + context_length].tolist())
        X = torch.tensor(X)
        Y = torch.tensor(Y)
        print(X.shape, Y.shape)
        return X, Y
