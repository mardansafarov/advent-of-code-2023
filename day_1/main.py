DIGITS_MAPPING = {'one': '1',
                  'two': '2', 
                  'three': '3', 
                  'four': '4', 
                  'five': '5', 
                  'six': '6', 
                  'seven': '7', 
                  'eight': '8', 
                  'nine': '9'}

sum = 0

def digit_in_string(word):
    for digit in DIGITS_MAPPING.keys():
        if digit in word:
            return digit
    return None
    
with open('input.txt', 'r') as f:
    for line in f:
        digit = ''
        letters_first = ''
        letters_last = ''
        for letter in line:
            if letter.isdigit():
                digit += letter
                break

            letters_first +=letter
            if digit_in_string(letters_first) != None:
                string_digit_1 = digit_in_string(letters_first)
                digit += DIGITS_MAPPING[string_digit_1]
                break
                
        for letter in reversed(line):
            if letter.isdigit():
                digit += letter
                break

            letters_first = letter + letters_first
            if digit_in_string(letters_first) != None:
                string_digit_2 = digit_in_string(letters_first)
                digit += DIGITS_MAPPING[string_digit_2]
                break
        
        sum += int(digit)
        
    print(sum)

