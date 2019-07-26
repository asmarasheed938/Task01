#accepts a string and calculate the number of digits and letters
vlaue=input("Enter a String: ")
digit=0
alpha=0
for i in vlaue:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        digit+=1
print("Number of digits: ",digit)
print("Number of aplhabets: ",alpha)