import sys
sys.stdin = open("input.txt",'r')
sys.stdout = open("output.txt", "w")

num1 = [1,2,2,1]
num2 = [2,2]
result = []
for i in num1:
	if i in num2:
		num2.remove(i)
		result.append(i)

print(result)