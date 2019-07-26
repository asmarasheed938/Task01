#get the smallest number from a list
my_list=[1,2,-8,0]
min=my_list[0]
for i in my_list:
    if min>i:
        min=i
print(min)