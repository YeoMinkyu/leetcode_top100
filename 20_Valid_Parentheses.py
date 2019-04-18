class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        open_list = []
        answer = {'(': ')', '{': '}', '[': ']'}
        result = True

        if s[0] == ')' or s[0] == '}' or s[0] == ']':
            return False

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                open_list.append(ch)
            else:
                if not open_list:
                    return False
                open_ch = open_list.pop()
                if answer[open_ch] != ch:
                    return False

        if open_list:
            return False

        return result
