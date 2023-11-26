import re

print("Instruction:type in what kind of number system do you have and to what number system you want it to be converted")
print("note: type the given in the format Given: value numtype")
print("")

inptype = input("From:")
anstype = input ("To: ")

#conversion from binary to decimal
if (inptype == "binary" and anstype == "decimal"):
    givenval = input("given:")
    iterval = "1"

    def iterate(givenval, iterval):
        indeces = []
        for i, char in enumerate(givenval):
            if char in iterval:
                indeces.append(i)
        print(f"The indices of characters '{iterval}' are: {indeces}")
        

    
