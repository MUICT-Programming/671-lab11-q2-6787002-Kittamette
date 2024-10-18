# YOUR CODE HERE
# YOUR CODE HERE
lsta = []
lstb = []
updated_list = []
min_max = []
def summation(lsta,lstb):
    global updated_list
    n = int(input())
    for i in range(n):
        x = int(input())
        lsta.append(x)
    for j in range(n):
        x = int(input())
        lstb.append(x)
    for i in range(n):
        a = lsta[i]
        b = lstb[i]
        sum = a+b
        updated_list.append(sum)
    return updated_list
def find_min_max():
    global updated_list,min_max
    updated_list.sort()
    min_max.append(updated_list[0])
    min_max.append(updated_list[-1])
    min_max = (tuple(min_max))

summation(lsta,lstb)
print(updated_list)
find_min_max()
print(min_max)
