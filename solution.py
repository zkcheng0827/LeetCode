# 739. Daily Temperatures
# my solution 49%
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) <= 1:
            return [0] * len(T)
        day_till_warmer = []
        value_stack = []
        index_stack = []
        distance = 1
        for i, a in enumerate(reversed(T)):
            while len(value_stack) > 0 and a >= value_stack[-1]:
                value_stack.pop(-1)
                index_stack.pop(-1)
            if len(index_stack) == 0:
                count = 0
            else:
                count = i - index_stack[-1]
            day_till_warmer.append(count)
            value_stack.append(a)
            index_stack.append(i)
        return list(reversed(day_till_warmer))
# better solution 88 %
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        inputArrayLength = len(T)
        result = [0] * inputArrayLength
        stack = deque()
        for i in range(inputArrayLength - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            stack.append(i)
        return result
