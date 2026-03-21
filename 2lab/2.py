def isPalindrome(s):
    clean = "".join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car"))                     # False
print(isPalindrome(" "))                              # True