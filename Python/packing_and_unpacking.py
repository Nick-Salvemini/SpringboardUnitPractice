names = ['bob', 'jill']
name1, name2 = names

# name1 returns 'bob'
# name2 returns 'jill'

point = (100, 58)
x,y = point

# x returns 100
# y returns 58

sorted_scores = [2400, 2350, 2100, 1960]
top_score, *scores = sorted_scores

# top_score returns 2400
# scores returns [2350, 2100, 1960]

color_pairs = [['red', 'green'], ['purple', 'orange']]
# pair1, pair2 = color_pairs

# piar1 returns ['red', 'green']
# pair2 returns ['purple', 'orange']

((primary1, secondary2), (primary2, secondary2)) = color_pairs
# must use parens to single a tuple

# primary1 returns 'red'
# secondary2  returns 'green'
# primary2 returns 'purple' 
# secondary2 returns 'orange'

grades = {'A' : 12, 'B': 19, 'C': 30}

for (k,v) in grades.items():
    print(k,v)