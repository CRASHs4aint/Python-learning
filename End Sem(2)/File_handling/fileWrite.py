file=open("example.txt","w") #create and overwrite file
file.write("Python is fun !\nWe are learning file handling")
file.close()

file=open("example.txt ","r")
content=file.read()
print(content)
file.close()

file=open("example.txt ","r")
for line in file:
    print(line.strip()) #.strip() removes newline characters
file.close()

file=open("example.txt ","a")
file.write("\nAppending newLine to the file.")
file.close()