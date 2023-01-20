# READING A FILE

# file = open('files2.txt', 'r')

# for line in file:
#     print('line =', line)

# file.seek(0)

# all_text = file.read()
# run like this, all_text will print an empty string, because you've already iterated over the file in the for loop.  it leaves you at the end, like finishing a vhs

# file.close()
# best practice is to close file at the end

# WRITING A FILE
def morse_to_letter(code):
    morse_chars = {'..-.': 'F', '-..-': 'X',
                 '.--.': 'P', '-': 'T', '..---': '2',
                 '....-': '4', '-----': '0', '--...': '7',
                 '...-': 'V', '-.-.': 'C', '.': 'E', '.---': 'J',
                 '---': 'O', '-.-': 'K', '----.': '9', '..': 'I',
                 '.-..': 'L', '.....': '5', '...--': '3', '-.--': 'Y',
                 '-....': '6', '.--': 'W', '....': 'H', '-.': 'N', '.-.': 'R',
                 '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D', '--.-': 'Q',
                 '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A', '...': 'S', '.----': '1'}
    return morse_chars.get(code, '')

def get_english(phrase):
    letters = phrase.split(' ')
    return ''.join([morse_to_letter(letter) for letter in letters])

# # file = open('files3.txt', 'w')
# # w = write, which will overwrite what is already in the file
# file = open('files3.txt', 'a')
# # a= append, which will add to the existing content
# file.write('\nI am another line')
# file.close()

# file = open('files4.txt', 'w')
# # since this file doesn't exist, it creates a new file
# file.write('i am a new file')
# file.close()

file = open('files2.txt', 'r')
translate = open('files5.txt', 'w')
# opening the first file in read mode to read each line of text, then create a new file in write mode to add new text after looping over the lines in the first file

for line in file:
    translate.write(get_english(line))

file.close()
translate.close()