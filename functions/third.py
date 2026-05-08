def palindrome(s):
    rev = ""
    for i in range(len(s)-1,-1,-1):
        rev = rev + s[i]
    if rev == s:
        print("palindrome")
    else:
        print("Not a palindrome")

palindrome("NAMAN")
palindrome('CURSOR')