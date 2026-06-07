class Solution:
    def isValid(self, s: str) -> bool:
        closed = []
        closing_dict = { ")": "(", "}":"{", "]":"["}
        for bracket in s:
            if bracket in closing_dict:
                if closed and closed[-1] == closing_dict[bracket]:
                    closed.pop()
                else:
                    return False
            else:
                closed.append(bracket)
        return True if not closed else False

