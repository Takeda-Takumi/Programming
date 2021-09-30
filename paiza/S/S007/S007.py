s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def search(strings):
    changes = {i: 0 for i in alphabet}
    strings_n = len(strings)
    strings = strings + '#'
    i = 0
    while i < strings_n:
        while True:
            if(strings[i] == '#'):
                return changes    
            elif(strings[i] != '(' and (not strings[i].isdecimal()) and strings[i] != ')'):
                changes[strings[i]] = changes[strings[i]] + 1
            else:
                break
            i += 1

        number = ''
        number_start = i
        while strings[i].isdecimal():
            number += strings[i]
            i += 1
        if(len(number) != 0):
            number_int = int(strings[number_start:i])
        else:
            number_int = 1
        
        if(strings[i] != '('):
            changes[strings[i]] = changes[strings[i]] + number_int
        else:
            quote_count = 0
            stringpart_start = i+1

            while True:
                if(strings[i] == '('):
                    quote_count += 1
                if(strings[i] == ')'):
                    quote_count -= 1
                if(quote_count == 0):
                    break
                i += 1
            stringpart = strings[stringpart_start:i]
            tmp = search(stringpart)
            for k in alphabet:
                changes[k] = changes[k] + tmp[k]*number_int
        i += 1
    return changes


alphabet_count = search(s)

for i in alphabet:
    print(i,alphabet_count[i])