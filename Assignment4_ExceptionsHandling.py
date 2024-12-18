# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
with open('Output1.txt', 'r') as file:
    print(file.read())

file = open('Output2.txt', 'w')
file.write("I Love python very much!")
file.close()

file = open('Output2.txt', 'a')
file.write("\nPlease join me!")
file.close()

# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
# Outcomes 🎉

try:
    with open('Output.txt', 'r') as file:
      print(file.read())

except FileNotFoundError: 
  print("File does not exist!. Please check the file name or create the file before it can be read?")
finally:
    file.close()


