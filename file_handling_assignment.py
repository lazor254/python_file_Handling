# opening file in write mode and writing three lines of text

with open("my_file.txt", 'w') as file:
    file.write("Hello lazor, this is line 1. \n")
    file.write("This is line two with some numbers: 12345.\n")
    file.write("Third line just to conclude.\n")


with open("my_file.txt", 'r') as file:
    print("Reading the contents of 'my_file.txt:")
    contents = file.read()
    print(contents)

with open("my_file.txt", 'a') as file:
    file.write("This is the append line 4.\n")
    file.write("Appending line 5 with a number: 2540.\n")
    file.write("I just added this as line six to show it really works.\n")

with open("my_file.txt", 'r') as file:
    print("Reading the contents of 'my_file.txt' after appending:")
    contents = file.read()
    print(contents)
