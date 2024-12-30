###

# bmrs
def bmrs(word,i=1):
    if not word.startswith(''):
        word =''+word
    if -1 < i< len(word):
        return interpret(word,i)+ bmrs(word, i+1)
    return ""


# predecessor
def p(word, i):
    if i <= 1:
        return 0
    else:
        return i-1

# successor
def s(word, i):
    if i >= len(word) - 1:
        return 0
    else:
        return i+1

#
def interpret(word, i):
    if H_o(word, i):
        return 'H'
    else:
        if L_o(word, i):
            return 'L'
        else:
            return '0'


