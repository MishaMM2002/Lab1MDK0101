x = 'Hello  world'
y = 'a word'

for i, words in enumerate((x, y)):
    a = [word for word in words.split()]
    print([a[0], a[0]][i])
