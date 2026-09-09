from typing import List, Dict

class Solution:
    def tokenize_numbers(self, numbers: List[int], vocab: Dict[str, int]) -> List[List[str]]:
        # Tokenize each number using greedy left-to-right longest match.
        # Return a list of token lists showing how each number gets split.
        
        output = []
        tokens = sorted(vocab.keys(), key=len, reverse=True)
        for num in numbers:
            result = []
            temp = str(num)
            while(temp):
                for token in tokens:
                    if temp.startswith(token):
                        result.append(token)
                        temp=temp[len(token)::]

                        break
            output.append(result)
        return output

    def count_tokens(self, text: str, vocab: Dict[str, int]) -> int:
        # Count how many tokens the text uses with greedy tokenization.
        # Use greedy left-to-right longest match.
        output = []
        tokens = sorted(vocab.keys(), key=len, reverse=True)
        while(text):
            for token in tokens:
                if text.startswith(token):
                    output.append(token)
                    text=text[len(token)::]
                    break
        return len(output)


    def fertility_score(self, text: str, vocab: Dict[str, int]) -> float:
        # Compute tokens-per-word ratio (fertility).
        # Higher = more expensive and less efficient.
        # Round to 4 decimal places.
        len_output = self.count_tokens(text,vocab)
        
        return round(len_output / len(text.split()),4)
