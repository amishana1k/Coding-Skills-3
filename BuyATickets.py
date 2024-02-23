from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = tickets[k]
        l = len(tickets)
        count = 0
        for i in range(l):
            count += min(tickets[i], t)
        return count
