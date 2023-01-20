lemon = {'sour', 'yellow', 'fruit', 'bumpy'}
banana = {'sweet', 'fruit', 'yellow', 'smooth'}
orange = ['fruit', 'bumpy', 'orange', 'sweet']

# intersection = lemon & banana
# difference = lemon - banana
# union = lemon | banana
# symmetric difference = lemon ^ banana

for adj in banana | lemon | set(orange):
    print(adj)

