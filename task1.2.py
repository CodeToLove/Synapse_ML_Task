
lst = ['0001','0011','0101','1011','1101','1111']

lst = [int(i,2) for i in lst]
lst.sort()
l = len(lst)
new_lst = []
i, j = 2, 3
new_lst.append(lst[0] + lst[l-1])
new_lst.append(lst[1] + lst[l-2]) 
while i < l//2 and j < l//2:
    new_lst[0] += lst[i] + lst[l - i -1]
    new_lst[1] += lst[j] + lst[l - j -1]
    i+=2
    j+=2
print(new_lst)
print(abs(new_lst[0]-new_lst[1]))