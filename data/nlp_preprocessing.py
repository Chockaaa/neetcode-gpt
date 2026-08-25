import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List

class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
        # 1. Build vocabulary: collect all unique words, sort them, assign integer IDs starting at 1
        # 2. Encode each sentence by replacing words with their IDs
        # 3. Combine positive + negative into one list of tensors
        # 4. Pad shorter sequences with 0s using nn.utils.rnn.pad_sequence(tensors, batch_first=True)
        words=[]
        for sentence in positive:
            words.extend(sentence.split())

        for sentence in negative:
            words.extend(sentence.split())

        new_list = sorted(set(words))

        new_list = sorted(set(words))
        word_to_num = {}
        for i in range(len(new_list)):
            word_to_num[new_list[i]] = float(i) + 1.0

        tensor = []
        for sentence in positive:
            tensor.append(torch.tensor([word_to_num[word] for word in sentence.split()], dtype=torch.float))
        for sentence in negative:
            tensor.append(torch.tensor([word_to_num[word] for word in sentence.split()], dtype=torch.float))

        output = nn.utils.rnn.pad_sequence(tensor, batch_first=True, padding_value=0.0)

        return output


