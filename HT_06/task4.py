# Створіть функцію <morse_code>, яка приймає на вхід рядок у вигляді
# коду Морзе та виводить декодоване значення (латинськими літерами).



def morse_code(code):
    morze = {'SOS': '...---...', 'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ': ''}
    count = 0
    result = []
    word_list = code.split(' ')
    for word in word_list:
        if word == '':
            count += 1
            if count == 2:
                count = 0
                continue
        for key, value in morze.items():
            if word == value:
               result.append(key)
        
    return ''.join(result)
        

print(morse_code('--. . . -.- .... ..-- -...   .. ...   .... . .-. .'))
print(morse_code('...---...'))
