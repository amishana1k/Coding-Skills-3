from typing import List

class Solution:
    def restoreString(self, k: str, v: List[int]) -> str:
        char_map = {pos: char for pos, char in zip(v, k)}

        sorted_char_map = sorted(char_map.items())

        restored_string = ''.join(char for _, char in sorted_char_map)
        
        return restored_string
