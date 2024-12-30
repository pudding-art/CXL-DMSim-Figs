# word = "H000L000"
# word = "00000L00000H"
# word = "00LH"
# word = "0HL0"
word = "00L00H00L00L"
word = list(word)
loc_h = -1
loc_l = -1

print("old version:",word)

for i  in range(len(word)):
    if word[i] == "0":
        continue
    if word[i] == "H":
        loc_h = i
    else:
        loc_l = i


print(loc_h)
print(loc_l)
# H在L前面然后 长度>=3
if(loc_l != -1 and loc_h < loc_l):
    word[loc_h] = '0'
    word[loc_l-1] = 'H'

if(loc_l!=-1 and loc_h > loc_l):
    if(loc_h-1==loc_l and loc_h==len(word)-1):
        word[loc_h] = '0'
    elif(loc_h-1!=loc_l):
        word[len(word) - 2] = 'H'
        word[loc_h] = '0'

if(loc_l == -1):
    word[loc_h] = '0'
    word[len(word)-2] = 'H'

print("new verison:", word)
