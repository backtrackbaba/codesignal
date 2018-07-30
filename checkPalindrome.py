
# a = 
# print(a[::-1])
inputString = "asdfgfdsa"
def checkPalindrome(inputString):
    pal = False
    if inputString == inputString[::-1]:
        pal = True
        return True
    else:
        return pal

print(checkPalindrome(inputString))