for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}x{i}={i*j}\t', end='')
    print()

# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while(j <= i):    # j的大小是由i来控制的
        print(f'{i}*{j}={i*j}', end='\t')
        j += 1
    print('')
    i += 1
