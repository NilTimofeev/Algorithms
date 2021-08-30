num = 100
num_list = [i for i in range(0, num + 1)]
num_list[1] = 0
for i in range(2, num):
    if num_list[i] != 0:
        for j in range(i + i, num + 1, i):
            num_list[j] = 0
res_list = [num for num in num_list if num > 0]
print(res_list)
