n = input().split(' ')
responseH = str(12 - int(n[0]))
responseM = str(60 - int(n[1]))
if len(responseH) == 1:
    responseH = '0' + responseH
if len(responseM) == 1:
    responseM = '0' + responseM
if responseM == '60':
    responseM = '00'
if n[0] == '0' or n[0] == '00':
    responseH = '00'
print(responseH + ':' + responseM)