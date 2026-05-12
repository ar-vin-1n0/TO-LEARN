#FILE HANDLING

#file handling is used to read,write,update and processing data in a file

#Basic file handling


#writing in a file
with open("example.txt","w") as f: #used to open file ,with is used to be default as it closes the file automatically without the close command

    f.write("hi")   #writing into a file

    #content = f.read()   #reading a file

    #line = f.readline()  #reads line by line now it only print the 1st line

    #"\n" new line character writes to a newline
    f.write("how are you") #without "\n"
    f.write("\ni am fine\n") # with "\n"


#reading a file
with open("example.txt","r") as f:

     content = f.read()   #reading a file

     line = f.readline()  #reads line by line now it only print the 1st line

     #Iteration in file objects

     for line in f:
         print(line.strip())


#appending in a file
#"w" mode writes file from scratch meaning if u open file with "w" it will delete all previous data in file to write new ones
#"a" mode append new line of data to the file without removing existing data it starts add data from the end

with open("example.txt","a") as f:
    f.write("hi")


# File Modes — VERY IMPORTANT

#| Mode | Meaning |
#| `"r"` | read |
#| `"x"` | create new file |
#| `"rb"` | binary read |
#| `"wb"` | binary write |
