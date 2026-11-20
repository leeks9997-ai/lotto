votes = ['짜장', '짬뽕','짜장','볶음밥','짜장','짬뽕']

count = {}
for menu in ['짜장', '짬뽕', '볶음밥']:
    count[menu] = 0
for v in votes:
    count[v] += 1

print(count)