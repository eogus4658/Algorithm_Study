arr = input().split('.')
res = ''
bTmp = True
for s in arr:
  res += 'AAAA' * (len(s) // 4)
  if (len(s) % 4) % 2 != 0:
    bTmp = False
    break
  elif len(s) % 4 == 2:
    res += 'BB'
  res += '.'
if bTmp:
  print(res[:-1])
else:
  print(-1)
