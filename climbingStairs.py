class Solution:
    def __init__(self):
        self.count = 0
        
    def climbStairs(self, n: int) -> int:
        arr = []
        arr.append(1)
        arr.append(1)
        for i in range(2, n+1):
            arr.append(arr[i-2]+arr[i-1])

        return arr[-1]
