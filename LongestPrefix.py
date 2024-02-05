class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()

        s = strs[0]
        for i, char in enumerate(s):
            for other_string in strs[1:]:
                if i >= len(other_string) or other_string[i] != char:
                    return s[:i]
        return s

solution = Solution()
strs = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs))
