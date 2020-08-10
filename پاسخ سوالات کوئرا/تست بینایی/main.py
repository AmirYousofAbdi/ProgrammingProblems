n = int(input())
v_1 = input()
v_2 = input()
t = 0
for i in range(0, n):
    if v_1[i] != v_2[i]:
        t += 1
print(t)
