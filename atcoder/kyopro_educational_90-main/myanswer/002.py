n = int(input())

def isEncyclopediaOfParentheses(string):

    string_changed = string
    string_changed_length = len(string_changed)
    i = 1
    while string_changed_length > 0 and i < string_changed_length:
        if(string[i-1] == '(' and string[i] == ')'):
            if(i == 1):
                string_changed = string[2:]
            elif(i == n-1):
                string_changed = string[:n-2]
            else:
                string_changed = string[0:i-1] + string[i+1:n]
            i = 1
            string = string_changed
            string_changed_length = len(string_changed)
            continue
        i += 1
    if(string_changed_length == 0):
        return True
    else:
        return False
    







for i in range(1<<n):
    s = ''
    for j in range(n):
        if((i >> j) & 1):
            s += '('
        else:
            s += ')' 

    if(isEncyclopediaOfParentheses(s)):
        print(s)


    

