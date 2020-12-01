f = open('day1.txt', 'r')
lst = []
for item in f:
    lst.append(int(item))

def twoSum(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if lst[i] + lst[j] == 2020:
                return [lst[i],lst[j]]

result1 = twoSum(lst)[0]
result2 = twoSum(lst)[1]

print(result1 * result2)