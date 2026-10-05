print("Program 5")
word1 = input("Enter word1: ").replace(" ", "").lower()
word2 = input("Enter word2: ").replace(" ", "").lower()
 
if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not an Anagram")
 
