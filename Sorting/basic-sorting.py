import sys
sys.stdin = open("../input.txt",'r')
sys.stdout = open("../output.txt", "w")

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)