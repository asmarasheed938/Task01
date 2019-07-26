#check whether an alphabet is a vowel or consonant
val=input("Enter a alphabet to check: ")
while len(val)>1:
    val=input("please Enter a alphabet: ")
cons=['a','e','i','o','u']
if val in cons:
    print("Entered alphabet is a VOWEL")
else:
    print("Entered alphabet is a CONSONANT")