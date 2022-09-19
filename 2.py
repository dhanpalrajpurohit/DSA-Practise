import sys
sys.stdin = open("input.txt",'r')
sys.stdout = open("output.txt", "w")

def permute(nums: List[int]) -> List[List[int]]:
    if len(nums)==0:
        return []
    if len(nums)==1:
        return [nums]
    lst = []
    for i in range(len(nums)):
        first = nums[i]
        reminder = nums[:i]+nums[i+1:]
        for p in permute(reminder):
            lst.append([first]+p)
    return lst