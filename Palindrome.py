def is_Palindrome(string):
    if string == "":
        return "Not Palindrome"
    else:
        new_str = ""
        for i in string.lower():
            if i.isalpha():
                new_str += i
        if new_str == new_str[::-1]:
            return "Palindrome"
        else:
            return "Not Palindrome"
            
s = input("Enter: ")
print(is_Palindrome(s))
