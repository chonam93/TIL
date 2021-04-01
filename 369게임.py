# 369게임만들기

final = int(input('얼마까지 369할까? '))

for i in range(1, final+1):
    cnt = 0
    for j in str(i):
        int_j = int(j)
        if int_j % 3 == 0 and int_j != 0:
            cnt += 1
    if cnt != 0:
        print(i, '->', 'clap!! '*cnt)
    if cnt == 0:
        print(i, '->', i)


