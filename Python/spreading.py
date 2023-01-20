nums = [2,4,6,8]

[0,*nums, 10]
# returns [0,2,4,6,8,10]

odds = [1,3,5,7,9]

[*odds, *nums]
# returns [1,3,5,7,9,2,4,6,8]

hello = [*'hello']
# returns ['h', 'e', 'l', 'l', 'o']

rainfall = {'Jan': 2.5, 'Feb': 4.9}
more_rainfall = {'Mar': 5.1, **rainfall}
# returns {'Mar': 5.1, 'Jan': 2.5, 'Feb': 4.9}

nums = [1,2,3,4,5,6,7,8,9]
print(nums)
# returns [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*nums)
# returns 1 2 3 4 5 6 7 8 9