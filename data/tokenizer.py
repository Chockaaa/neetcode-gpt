from typing import List


class Solution:
    def get_merges(self, corpus: str, num_merges: int) -> List[List[str]]:
        # 1. Split corpus into a list of individual characters
        # 2. For each merge step:
        #    a. Count frequency of all adjacent token pairs
        #    b. Find the most frequent pair (break ties lexicographically)
        #    c. Merge all non-overlapping occurrences left to right
        #    d. Record the merge as [token_a, token_b]
        # 3. Return the list of merges performed
        list_of_merges = []
        corpus_bank = list(corpus)

        for _ in range(num_merges):
            frequencies = self.getFreq(corpus_bank)
            max_freq = max(frequencies.values())
            max_keys = [k for k, v in frequencies.items() if v == max_freq]
            
            smallest_lex_key = min(max_keys)
            new_corpus_bank,token_a_and_b = self.mergelex(smallest_lex_key,corpus_bank)
            corpus_bank = new_corpus_bank.copy()
            print(corpus_bank)
            list_of_merges.append(token_a_and_b)

        return list_of_merges


    def getFreq(self,token):
        first = token[:-1]
        second = token[1:]
        bank = {}
        for i in range(len(first)):
            if (first[i], second[i]) in bank:
                bank[(first[i], second[i])] +=1
            else:
                bank[(first[i], second[i])] = 1
        return bank

    def mergelex(self,maxFreq_pair,corpus_bank):
        new_corpus_bank=[]
        i=0
        while(i < len(corpus_bank)-1):
            print(new_corpus_bank)
            pair = (corpus_bank[i], corpus_bank[i+1])
            if (maxFreq_pair == pair ):
                new_corpus_bank.append(corpus_bank[i]+ corpus_bank[i+1])
                token_a_and_b = [corpus_bank[i], corpus_bank[i+1]]
                i+=2
                
            else:
                new_corpus_bank.append(corpus_bank[i])
    
                i+=1
        if i <= len(corpus_bank)-1:
            new_corpus_bank.append(corpus_bank[i])
        return new_corpus_bank,token_a_and_b
