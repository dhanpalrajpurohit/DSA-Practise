import sys
sys.stdin = open("input.txt",'r')
sys.stdout = open("output.txt", "w")

t = unsigned(input())
print(t)
count = 0
while t>0:
	if (t&1==1):
		count+= t & 1
	t = t>>1
print(count)
