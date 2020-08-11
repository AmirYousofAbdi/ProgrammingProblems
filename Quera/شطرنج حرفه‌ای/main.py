n = input()
n_copy = 0
tedad_moshakhas = [1, 0, 1, 0, 2, 0, 2, 0, 2, 0, 8]
tedad_ezafe_shode = []
jam = ''
for i in range(0, len(tedad_moshakhas), 2):
    if len(tedad_ezafe_shode) <= 5:
        komaki = tedad_moshakhas[i]
        if n[i] != ' ':
            komaki2 = n[i]
            tedad_ezafe_shode.append(int(komaki) - int(komaki2))
for i in range(0, len(tedad_ezafe_shode)):
    jam += str(tedad_ezafe_shode[i]) + ' '
print(jam)