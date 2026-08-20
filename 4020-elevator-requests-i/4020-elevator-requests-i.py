class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        
        result=0
        for i in range(len(requests)-1):
            result+=abs(requests[i]-requests[i+1])

        return result+requests[0]

        