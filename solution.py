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
    
# 647. Palindromic Substrings
# bad 28%
    def countSubstrings(self, s: str) -> int:
        ret = set([(i, i) for i in range(len(s))])
        for len_i in range(2, len(s) + 1):
            for i in range(0, len(s) - len_i + 1):
                j = i + len_i - 1
                if s[i] == s[j]:
                    if len_i <= 2 or (i + 1, j - 1) in ret:
                        ret.add((i, j))
        return len(ret)
# ok 38%
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        if size <= 1:
            return size
        last_set = [(i, i) for i in range(len(s))]
        last_set.extend([(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]])
        all_set = set(last_set)
        while True:
            new_set = []
            for i, j in last_set:
                if j < len(s) - 1 and i > 0 and s[i - 1] == s[j + 1]:
                    new_set.append((i - 1, j + 1))
            if len(new_set) == 0:
                break
            last_set = new_set
            all_set.update(set(new_set))      
        return len(all_set)
# Manacher's Algorithm 
# 99% not me
    def countSubstrings(self, s: str) -> int:
        def manacher(s):
            t = "&#" + "#".join(s) + "#@"
            n = len(t)
            p, c, r, val = [0]*n, 0, 0, 0
            for i in range(1, n-1):
                if r > i:
                    p[i] = min(p[2*c - i], r - i)
                while t[i+p[i]+1] == t[i-p[i]-1]:
                    p[i] += 1
                if i + p[i] > r:
                    c, r = i, i + p[i]
            return p
        return sum((v+1)//2 for v in manacher(s))
    
# Merge Two Binary Trees
# 47%
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None or t2 is None:
            return t1 if t2 is None else t2
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
# iterative
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        stack = []
        stack.append((t1, t2))
        while stack:
            t = stack.pop()
            if t[1] is None:
                continue
            t[0].val += t[1].val
            if t[0].left is None:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            if t[0].right is None:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1


# 448. Find All Numbers Disappeared in an Array
# 49%
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] != i + 1:
                while nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                    tmp = nums[i]
                    nums[i] = nums[tmp - 1]
                    nums[tmp - 1] = tmp
        missing = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                missing.append(i + 1)
        return missing
