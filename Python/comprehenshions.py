nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# evens  = []
# for num in nums:
#     if num%2 == 0:
#         evens.append(num)

# print(evens)

# ooooooor

# evens = [num for num in nums if num % 2 == 0]

[num * 2 for num in nums]

new_list = []
for num in nums:
    new_list.append(num*2)

hi_list = ['HIIII' for num in nums]

# [what_to_append for thing in list]

num_list = [2,4,6,8]
square_list = [num*num for num in num_list]

# print(square_list)

# print ([char.upper() for char in 'lmfao'])

# print([num for num in range(10,20)])



# board = [[0 for y in range(3)] for x in range(3)]
# print(board)

def gen_board(num_of_cols, num_of_rows, initial_val=None):
    board = [[initial_val for col in range(num_of_cols)] for row in range(num_of_rows)] 
    print(board)


# print([x * 2 for x in range(10) if x % 2 == 0])



chickens = [
    {'name': 'Henry', 'sex': 'rooster'},
    {'name': 'Jenn', 'sex': 'hen'},
    {'name': 'Bob', 'sex': 'rooster'},
    {'name': 'Bill', 'sex': 'rooster'},
    {'name': 'Lil', 'sex': 'hen'},
    {'name': 'Gill', 'sex': 'hen'},
]

hens = [chicken['name'] for chicken in chickens if chicken['sex'] == 'hen']
# print(hens)


# for if else statements [do_this if something else do_this for thing in things]

scores = [55, 89, 99, 87, 60, 70, 74, 76, 50, 90, 82]
grades = ['Pass' if score >= 70 else 'Fail' for score in scores]
# print(grades)

def get_letter(ltr): 
    morse_code_lookup = {
    'A':'.-', 'B':'-...','C':'-.-.', 
    'D':'-..', 'E':'.','F':'..-.', 
    'G':'--.', 'H':'....','I':'..', 
    'J':'.---', 'K':'-.-','L':'.-..', 
    'M':'--', 'N':'-.','O':'---', 
    'P':'.--.', 'Q':'--.-','R':'.-.', 
    'S':'...', 'T':'-','U':'..-', 
    'V':'...-', 'W':'.--','X':'-..-', 
    'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', 
    ', ':'--..--', '.':'.-.-.-','?':'..--..', 
    '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'
    }
    return morse_code_lookup.get(ltr.upper(), '')

msg = [get_letter(char) for char in 'SOS']

# print(msg)

def get_word_in_morse_code(str):
    return '   '.join([get_letter(char) for char in str])



# DICTIONARY COMPREHENSIONS 

eggs_per_day = {day:0 for day in 'MTWRFSU'}
# print(eggs_per_day)

squares_dict = {num: num * num for num in range(1,10)}
# print(squares_dict)

squares_dict_even = {num: num * num for num in range(1,10) if num % 2 == 0}
# print(squares_dict_even)


# Set Comprehensions - same as dictionaries, but without k/v pairs

set_comp = {char for char in 'abracadbaraalacazam'}
print(set_comp)

set_comp2 = {char for char in 'hello darkness my old friend' if char not in 'aeiou'}
print(set_comp2)