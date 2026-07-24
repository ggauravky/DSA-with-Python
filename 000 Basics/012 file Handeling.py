## File Handling in Python
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# types of file modes
# r - read mode
# w - write mode
# a - append mode
# x - exclusive creation
# b - binary mode
# t - text mode (default)

# another way to read file
f = open("file.txt", "r")
content = f.read()
print(content)
f.close()


# # Writing to a file
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is a test file.\n")
    
# # Appending to a file
with open("file.txt", "a") as f:
    f.write("Appending a new line.\n")
    f.write("Another line appended.\n")
    
# # Reading a file line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())
        
# # Reading a file using readlines()
with open("file.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        
        