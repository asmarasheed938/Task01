#find the second smallest number in a list.
my_list=[1, 2, -8, -2, 0]
if len(my_list)<2:
    print("No 2nd Minimum in this list exist!")
elif len(my_list)==2:
    if my_list[0]>my_list[1]:
        print("2nd Minimum is ",my_list[0])
    elif my_list[0]<my_list[1]:
        print("2nd Minimum is ", my_list[1])
    else:
        print("No 2nd Minimum in this list exist!")
else:
    my_list.sort()
    print("2nd Minimum is ", my_list[1])