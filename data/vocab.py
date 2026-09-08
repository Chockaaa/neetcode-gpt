from typing import Dict, List, Tuple

class Solution:
    def build_vocab(self, text: str) -> Tuple[Dict[str, int], Dict[int, str]]:
        # Return (stoi, itos) where:
        # - stoi maps each unique character to a unique integer (sorted alphabetically)
        # - itos is the reverse mapping (integer to character)
        print(text)
        text = sorted(text)
        stoi = {}
        itos = {}
        num = 0
        for i in text:
            if i in stoi:
                pass
            else:
                stoi[i] = num
                itos[num] = i
                num+=1

        return (stoi,itos)
        

    def encode(self, text: str, stoi: Dict[str, int]) -> List[int]:
        # Convert a string to a list of integers using stoi mapping
        mapping = []
        for i in text:
            mapping.append(stoi[i])
        return mapping

    def decode(self, ids: List[int], itos: Dict[int, str]) -> str:
        # Convert a list of integers back to a string using itos mapping
        mapping = []
        for i in ids:
            mapping.append(itos[i])
        return ''.join(mapping)
