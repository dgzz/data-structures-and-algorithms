# 斐波那契数列：简单地说，起始两项为 0 和 1，
# 此后的项分别为它的前两项之和。

def fibo(num):
    if num == 1:
        fibo_list = [1]
    elif num == 2:
        fibo_list = [1,1]
    else:
        fibo_list = [1, 1]
        for i in range(2, num):
            fibo_list.append(fibo_list[i - 2] + fibo_list[i - 1])
    return fibo_list

print(fibo(3))
