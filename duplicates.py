len_a = int(input("Give size for 1st list: "))
if len_a == 0:
    len_a = int(input("Give size for 1st list: "))
a = set([int(input("Give a number for 1st list->")) for i in range(len_a)])
len_b = int(input("Give size for 2nd list: "))
if len_b == 0:
    len_b = int(input("Give size for 2ns list: "))
b = set([int(input("Give a number for 2nd list->")) for i in range(len_b)])
print("Similar elements are: ", *(a & b))
