n = int(input())
jam = ''
for i in range(1, n + 1):
    for j in range(1, n + 1):
        jam += str(i * j) + ' '
    print(jam)
    jam = ''