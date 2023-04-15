def t(k):
    m = list()
    for s , h in k.items():
      m.append((s,h))
    return m

print(t({'Red': 1 , 'Green': 3 , 'White': 5 , 'Black': 2 , 'Pink': 4}))
