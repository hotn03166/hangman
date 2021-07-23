# 線形探索

def ss(num_list, n):
    found = False
    for i in num_list:
        if i == n:
            found = True
            break
    return found

numbers = range(0, 100)
print('search by 2 :' + str(ss(numbers, 2)))
print('search by 202 :' + str(ss(numbers, 202)))
