# num = 0

# print(num)
# while num < 100:
#     num += 10
#     print(num)


target = 37
guess = None

while guess != target:
    guess =  input('Please guess from 1 to 50')
    if guess == 'q' or guess == 'quit':
        break
    guess = int(guess)

print('all done')