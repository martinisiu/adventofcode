f = open('day1.txt', 'r')
lst = []
for item in f:
    lst.append(int(item))

def twoSum(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            for k in range(j, len(lst)):
                if lst[i] + lst[j] + lst[k] == 2020:
                    return lst[i] * lst[j] * lst[k]

print(twoSum(lst))