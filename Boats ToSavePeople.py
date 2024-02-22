class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        b = 0
        i = 0
        j = len(people) - 1
        
        p = sorted(people)
        
        while i <= j:
            if p[i] + p[j] <= limit:
                i += 1  # Move to the next lightest person
            j -= 1  # Move to the next heaviest person
            b += 1  # Assign a boat
            
        return b
