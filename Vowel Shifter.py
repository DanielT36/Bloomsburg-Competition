vowelslower = ["a","e","i","o","u","a"]
vowelsupper = ["A","E","I","O","U","A"]
output = ""
shiftee = str(raw_input("Enter a sentence you would like to shift: \n"))
for i in range (len(shiftee)):
    if shiftee[i] in vowelslower or shiftee[i] in vowelsupper:
        if shiftee[i].islower():
            output += vowelslower[vowelslower.index(shiftee[i])+1]
        else:
            output += vowelsupper[vowelsupper.index(shiftee[i])+1]
    else:
        output += shiftee[i]
print(output)