# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(string1, string2):
    # [assignment] Add your code here
    #convert both argument to lowercase
    string1 = string1.lower()
    string2 = string2.lower()

    #checking if sorted string are the same
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False


print(find_anagrams("Arc", "Car"))