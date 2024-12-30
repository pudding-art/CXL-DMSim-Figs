### Predefined functions - DO NOT CHANGE THESE ###

word = "0LHL000"
word = list(word)
# bmrs
# def bmrs(word, i=1):
#     if not word.startswith('_'):
#         word = '_' + word
#     if -1 < i < len(word):
#         return interpret(word, i) + bmrs(word, i + 1)
#     return ''




# predecessor 返回上一个字符的下标
def p(word, i):
    if i <= 1:
        return 0
    else:
        return i - 1


# successor 返回下一个字符的下标
def s(word, i):
    if i >= len(word) - 1:
        return 0
    else:
        return i + 1


# interpreter function
def interpret(word, i):
    # print("H_o:", H_o(word, i))
    # print("word:", word)
    if H_o(word, i):
        return 'H'
    else:
        if L_o(word, i):
            return 'L'
        else:
            return '0'


# 判断是否为H/L
# input predicate for high tones
def H_i(word, i):
    return word[i] == 'H'


# input predicate for low tones
def L_i(word, i):
    return word[i] == 'L'

##################################上面不能改
##################################下面俩能改 哪个更好改改哪个
#####1
def H_o(word, i):
    if (i == len(word) - 2 ):
        if  has_H(word, p(word,i)):
            return False
        else:
            return True
    if(i > len(word)-2):
        return False
    # 判断后面是否有L,如果有L
    elif has_L(word,s(word,i)):
        # 如果下一个字母就是L，返回H
        if L_i(word,s(word,i)):
            return True
        # 如果下一个字母不是L，要将H放到L前面
        else:
            #print("i=",i)
            word[s(word, i)] = 'H'
            return False


        return True
    else:
        return False

def L_o(word, i):
    if L_i(word,i):
        return True
    else:
        return False
# 判断word从i开始后面是否有L
def has_L(word,i):
    if L_i(word, i):
        return True
    else:
        if(i == len(word)-1):
            return False
        else:
            return has_L(word,s(word,i))
# 判断word从i往前是否有H
def has_H(word, i):
    if H_i(word,i):
        return True
    else:
        if(i == 0):
            return False
        else:
            return has_H(word,p(word,i))



# bmrs(word, 0)
word_new = ""
for i in range(len(word)):
    word_new = word_new + interpret(word,i)

print("new version", word_new)