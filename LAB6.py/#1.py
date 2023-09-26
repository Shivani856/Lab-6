char = input("Enter the string : ")
consonant = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
VOWELS = ['A','E','I','O','U']
consonant_i = 0
VOWELS_i = 0
for i in char:
    if i in consonant:
        consonant_i=consonant_i+1
    else:
        VOWELS_i+=1         
print("consonant",consonant_i)
print("VOWELS",VOWELS_i)
