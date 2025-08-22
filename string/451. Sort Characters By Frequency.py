# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.


# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

#Solution
class Solution:
    from collections import Counter
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        for ch, freq in cnt.items():
            buckets[freq].append(ch)
        res = []
        for freq in range(len(buckets)-1, 0, -1):
            for ch in buckets[freq]: #here is the count of the char in buckets
                res.append(ch * freq)
        return "".join(res)
