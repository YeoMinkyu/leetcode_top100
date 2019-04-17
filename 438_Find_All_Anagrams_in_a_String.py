from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        result = []
        counter_s = Counter(s[:len(p)-1])
        counter_p = Counter(p)

        for idx in range(len(p)-1, len(s)):
            if s[idx] in counter_s:
                counter_s[s[idx]] += 1
            else:
                counter_s[s[idx]] = 1

            if counter_s == counter_p:
                result.append(idx-len(p)+1)

            counter_s[s[idx - len(p)+1]] -= 1
            if counter_s[s[idx - len(p)+1]] == 0:
                del counter_s[s[idx - len(p)+1]]

        return result


if __name__ == "__main__":
    solution = Solution()
    solution.findAnagrams("cbaebabacd", "abc")
