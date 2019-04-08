number1 = int(input("Enter a positive integer: "))
number2 = int(input("Enter a second positive integer: "))
length = len(str(number1))
length2 = len(str(number2))

def carries():
    index1 = str(number1)
    index2 = str(number2)
    carry = 0
    carries = 0
    c1 = length
    c2 = length
    if (length < length2):
        while (c1 < length2):
            index1 = "0" + index1
            c1+=1
    if (length2 < length):
        while (c2 < length):
            index2 = "0" + index2
            c2+=1
    i = c1
    while (i > 0):
        if (int(index1[i-1])+int(index2[i-1])+carry > 9):
            carry = 1;
            carries+=1
        else:
            carry = 0
        i-=1
    return carries

print("There will be ",carries(),"carries.")