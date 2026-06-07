class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        sum = 0
        for op in operations:
            
            if op == "+":
                sum += (score[-1]+score[-2])
                score.append((score[-1]+score[-2]))
                print(f" op = {op}, score = {score}, sum = {sum}")
            elif op == "D":
                sum += 2*score[-1]
                score.append(2*score[-1])
                print(f" op = {op}, score = {score}, sum = {sum}")
            elif op == "C":
                sum -= score[-1]
                #print(f" op = {op}, score = {score}, sum = {sum}")
                score.pop()
                print(f" op = {op}, score = {score}, sum = {sum}")
            else:
                sum += int(op)
                score.append(int(op))
                
                print(f" op = {op}, score = {score}, sum = {sum}")
        print(score)

        return sum
        