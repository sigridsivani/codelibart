
# Print a blank line
print("\n")

# Ask the user for a filename
filename = input("Please enter the name of a file in this directory: ")

# Open that file
file = open(filename)

print("Name is: " + file.readline())
print("Title is: " + file.readline())
print("Phone number is: " + file.readline())
print("Address is: " + file.readline())

No new txt files were created, i typed test.py and this came up: Please enter the name of a file in this directory: test.py
Name is: x = 5

Title is: y = 10

Phone number is: if x > y: 

Address is:     print("Greater than fiiiiive!")