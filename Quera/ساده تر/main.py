def sefr(n):
    n = float(n)
    n = str(n)
    n = n.split('.')
    m = ''
    for i in range(6 - len(n[1])):
        m += '0'
    return n[0] + '.' + n[1] + m
n = []
for i in range(4):
    n.append(int(input()))
sum_1 = n[0] + n[1] + n[2] + n[3]
average_1 = sum_1 / 4
sum_1 = sefr(sum_1)
average_1 = sefr(average_1)
product_1 = n[0] * n[1] * n[2] * n[3]
product_1 = sefr(product_1)
max_1 = max(n)
max_1 = sefr(max_1)
min_1 = min(n)
min_1 = sefr(min_1)
k = ''
for i in sum_1:
    k += i
print('Sum : ', k)
k = ''
for i in average_1:
    k += i
print('Average : ', k)
k = ''
for i in product_1:
    k += i
print('Product : ', k)
k = ''
for i in max_1:
    k += i
print('MAX : ', k)
k = ''
for i in min_1:
    k += i
print('MIN : ', k)